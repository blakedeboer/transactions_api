from flask import Flask, request
from models import db
from flask_migrate import Migrate
from utils import get_row_objects

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


@app.route("/")
def welcome():
    return "Welcome. Use the /transactions enpoint to create and get transactions."

@app.route("/transactions", methods=["GET", "POST"])
def transactions_handler():
    if request.method == "POST":
        file = request.files["a_csv"]

        headers = get_headers_from_file(file)   #['Amount', 'Description']
        print("headers", headers)
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream)
        for row in csv_input:
            print(row)
            # ['Amount', ' Description']
            # ['-1.36', 'SWEETGREEN UNION SQUAR NEW YORK, NY, US']
            # ['200.16', 'PAYROLL~ Future Amount: 200.16 ~ Tran: DDIR']
        row_count = 10
        return f"you posted {row_count} transactions"
    else:
        return "you getted"

def get_headers_from_file(file):
    first_row_as_byte = file.stream.readline()
    first_row_as_string = first_row_as_byte.decode("UTF8")
    first_row_without_new_line_chars = first_row_as_string.rstrip("\n")
    return [header.strip() for header in first_row_without_new_line_chars.split(",")]

if __name__ == "__main__":
    app.run()