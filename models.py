from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    description = db.Column(db.String)

    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def __repr__(self):
        return "%s(%s)" % (self.__class__.name__, {
            column: value
            for column, value in self._to_dict().items()
        })