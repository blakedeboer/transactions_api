from flask import Flask, request
from models import db, Transaction
from flask_migrate import Migrate
from utils import get_row_objects
from file_processor.file_processor import FileProcessor

import csv
import io

app = Flask(__name__)

POSTGRES = {
    'db': 'mytransactionsdb',
    'host': 'localhost'
}   
    # 'port': '5432'
    # 'user': 'postgres',
    # 'pw': 'password',

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(host)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from models import db
    db.init_app(app)

    return app


@app.route("/")
def welcome():
    return "Welcome. Use the /transactions enpoint to create and get transactions."

@app.route("/transactions", methods=["GET", "POST"])
def transactions_handler():
    if request.method == "POST":
        file = request.files["a_csv"]
        processor = FileProcessor(file)
        rows = processor.process()
        for row in rows:
            amount = get_amount(row)
            description = row[" Description"]
            new_transaction = Transaction(amount, description)
            db.session.add(new_transaction)
        db.session.commit()
        row_count = len(rows)
        return f"you posted {row_count} transactions"
    else:
        return "you getted"


def get_amount(row):
    float_amt_with_cents = float(row["Amount"])
    return int(float_amt_with_cents*100)


# def get_headers_from_file(file):
#     first_row_as_byte = file.stream.readline()
#     first_row_as_string = first_row_as_byte.decode("UTF8")
#     first_row_without_new_line_chars = first_row_as_string.rstrip("\n")
#     return [header.strip() for header in first_row_without_new_line_chars.split(",")]

if __name__ == "__main__":
    app.run()