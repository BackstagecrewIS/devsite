from flask import render_template, request, redirect, url_for
from faq import app, db
from faq.models import Category, Question


@app.route("/")
def home():
    questions = list(Question.query.order_by(Question.question).all())
    return render_template("faq.html", questions=questions)


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
            answer="Coming Soon",
            category_id=10
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_question.html")
