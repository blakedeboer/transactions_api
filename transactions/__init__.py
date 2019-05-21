import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    POSTGRES = {
    'db': 'mytransactionsdb',
    'host': 'localhost'
}   
    # 'port': '5432'
    # 'user': 'postgres',
    # 'pw': 'password',
    
    app.config.from_mapping(
        DEBUG=True,
        SQLALCHEMY_DATABASE_URI='postgresql://%(host)s/%(db)s' % POSTGRES,
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    from models import db
    db.init(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app