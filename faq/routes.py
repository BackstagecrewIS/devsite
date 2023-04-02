from flask import render_template, request, redirect, url_for, flash, session
from faq import app, db
from faq.models import Category, Question, User
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    # Landing page
    return render_template(
        "main.html")


@app.route("/faq")
def faq():
    # Get questions and answeres for faq page
    questions = list(Question.query.order_by(Question.category_id).all())
    categories = list(Category.query.order_by(Category.id).all())
    return render_template(
        "faq.html", questions=questions, categories=categories)


# Contact Form
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        return render_template("thanks.html",
                               name=name,
                               email=email,
                               phone=phone,
                               message=message)
    return render_template(
        "contact.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # get form responses
        username = request.form.get("username").lower()
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        email = request.form.get("email")
        terms = request.form.get("terms")
        # Check if Terms & Conditions Checkbox ticked
        if terms != 'on':
            flash("You must agree to the Ts & Cs to register")
            return render_template("register.html")
        # Check both passwords match
        if password1 != password2:
            flash("Passwords don't match")
            return render_template("register.html")
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("User already exists")
            return render_template("register.html")
        # If all tests passed, create new user
        new_user = User(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password1")),
            email=request.form.get("email")
        )
        # Set user session
        session["user"] = request.form.get("username").lower()

        # Commit to database
        db.session.add(new_user)
        db.session.commit()
        flash("Registration Successful")

        # get user details back from database including id
        new_user = User.query.filter_by(username=username).first()

        # Set userid session
        session["userid"] = new_user.id
        return redirect(url_for('home', username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check user exists
        existing_user = User.query.filter_by(
            username=request.form.get("username").lower()).first()

        if existing_user:
            # Check password hash against database
            if check_password_hash(
                    existing_user.password, request.form.get("password")):
                # Set sessions
                session["user"] = request.form.get("username").lower()
                session["userid"] = existing_user.id

                # Check if administrator
                if existing_user.admin:
                    session["admin"] = "True"
                else:
                    session["admin"] = "False"

                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(
                    url_for('home', username=session["user"]))
            else:
                flash("Incorrect username or password")
                return render_template("login.html")
        else:
            flash("Incorrect username or password")
            return render_template("login.html")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out")
    return redirect(url_for("home"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if session["user"]:
        userid = session["userid"]
        questions = list(Question.query.filter_by(asked_by=userid).all())
        return render_template(
            "profile.html", questions=questions,
            username=username, userid=userid)

    return render_template("login.html")


@app.route("/categories")
def categories():
    if Category.query.filter_by(id=0).first():
        categories = list(
            Category.query.order_by(Category.category_name).all())
    else:
        flash("First Category Populated")
        initialise = Category(id=0, category_name="Admin")
        db.session.add(initialise)
        db.session.commit()

    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_question", methods=["GET", "POST"])
def add_question():
    if request.method == "POST":
        question = Question(
            question=request.form.get("question"),
            answer="Awaiting answer",
            category_id=0,
            asked_by=int(session["userid"])
        )

        db.session.add(question)
        db.session.commit()
        return redirect(url_for("faq"))
    return render_template("add_question.html")


@app.route("/admin_questions")
def admin_questions():
    questions = list(Question.query.order_by(Question.category_id).all())
    categories = list(Category.query.order_by(Category.id).all())
    return render_template(
        "admin_questions.html", questions=questions, categories=categories)


@app.route("/answer_question/<int:question_id>", methods=["GET", "POST"])
def answer_question(question_id):
    question = Question.query.get_or_404(question_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        question.question = request.form.get("question")
        question.answer = request.form.get("answer")
        question.category_id = int(request.form.get("category_id"))
        db.session.commit()
        return redirect(url_for("admin_questions"))
    return render_template(
        "answer_question.html", question=question, categories=categories)


@app.route("/delete_question/<int:question_id>")
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete_account/<int:userid>")
def delete_account(userid):
    user = User.query.get_or_404(userid)
    db.session.delete(user)
    db.session.commit()
    flash("Account Deleted")
    return redirect(url_for("logout"))
