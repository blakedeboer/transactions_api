from my_test import MyTest
from models import Transaction

class TestTransactions(MyTest):

    def test_something(self):
        transaction = Transaction(12, "thing")
        db.session.add(transaction)
        db.session.commit()
        assert transaction in db.session


# https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
# http://flask.pocoo.org/docs/1.0/testing/
# https://pythonhosted.org/Flask-Testing/
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/