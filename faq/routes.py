from flask import render_template
from faq import app, db
from faq.models import Category, Question


@app.route("/")
def home():
    return render_template("faq.html")
