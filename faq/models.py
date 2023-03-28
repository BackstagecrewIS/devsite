from faq import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    questions = db.relationship(
        "Question", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Question(db.Model):
    # schema for the Question model
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(250), nullable=False)
    answer = db.Column(db.Text, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey(
            "category.id", ondelete="CASCADE"), nullable=False)
    asked_by = db.Column(
        db.Integer, db.ForeignKey(
            "user.id", ondelete="CASCADE"))

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Question: {1} | Answer: {2}".format(
            self.id, self.question, self.answer
        )


class User(db.Model):
    # schema for the Users model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(210), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    questions = db.relationship(
        "Question", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return
        "#{0} Username: {1} | Password: {2} | Email: {3} | Admin: {4}".format(
            self.id, self.username, self.password, self.email, self.admin)
