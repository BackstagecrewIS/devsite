from faq import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship(
        "Question", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Question(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(250), unique=True, nullable=False)
    answer = db.Column(db.Text, unique=True, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey(
            "category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Question: {1} | Answer: {2}".format(
            self.id, self.question, self.answer
        )
