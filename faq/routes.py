from flask import render_template, request, redirect, url_for
from faq import app, db
from faq.models import Category, Question, User
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    questions = list(Question.query.order_by(Question.category_id).all())
    categories = list(Category.query.order_by(Category.id).all())
    return render_template(
        "faq.html", questions=questions, categories=categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        email = request.form.get("email")
        terms = request.form.get("terms")

        if terms != 'on':
            print ("Terms not accepted")

        if password1 != password2:
            print("Passwords don't match")

        if terms and (password1 == password2):
            print("Everything OK")



        print(username, password1, password2, email, terms)

    return render_template("register.html")


@app.route("/login")
def login():
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
            answer="We will answer soon",
            category_id=0
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_question.html")


@app.route("/answer_question/<int:question_id>", methods=["GET", "POST"])
def answer_question(question_id):
    question = Question.query.get_or_404(question_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        question.question = request.form.get("question")
        question.answer = request.form.get("answer")
        question.category_id = int(request.form.get("category_id"))
        db.session.commit()
        return redirect(url_for("home"))
    return render_template(
        "answer_question.html", question=question, categories=categories)


@app.route("/delete_question/<int:question_id>")
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for("home"))
