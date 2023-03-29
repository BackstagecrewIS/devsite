from flask import render_template, request, redirect, url_for, flash, session
from faq import app, db
from faq.models import Category, Question, User
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template(
        "main.html")


@app.route("/faq")
def faq():
    questions = list(Question.query.order_by(Question.category_id).all())
    categories = list(Category.query.order_by(Category.id).all())
    return render_template(
        "faq.html", questions=questions, categories=categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username").lower()
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        email = request.form.get("email")
        terms = request.form.get("terms")
        # Terms & Conditions Checkbox ticked
        if terms != 'on':
            flash("You must agree to the Ts & Cs to register")
            return render_template("register.html")
        # Passwords both match
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
        session["user"] = request.form.get("username").lower()
        db.session.add(new_user)
        db.session.commit()
        flash("Registration Successful")
        return render_template("login.html")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = User.query.filter_by(
            username=request.form.get("username").lower()).first()

        if existing_user:
            # flash("User Exists")
            if check_password_hash(
                    existing_user.password, request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                session["userid"] = existing_user.id
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
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("home"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if session["user"]:
        userid = session["userid"]
        questions = list(Question.query.filter_by(asked_by=userid).all())
        return render_template(
            "profile.html", username=username, questions=questions)

    return render_template("login.html")


@app.route("/categories")
def categories():
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
        return redirect(url_for("home"))
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
