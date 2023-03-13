from flask import render_template
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
    return render_template("add_category.html")
