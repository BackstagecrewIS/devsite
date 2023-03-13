from flask import render_template, request
from faq import app, db
from faq.models import Category, Question


@app.route("/")
def home():
    return render_template("faq.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
    return render_template("add_category.html")
