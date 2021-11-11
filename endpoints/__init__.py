from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT, jwt_required, current_identity
# from flask_cors import CORS, cross_origin
from os import path

db=SQLAlchemy()
DB_NAME="project_expenses.db"


def create_app():
    app = Flask(__name__)
    # cors = CORS(app, resources={r"*": {"origins": "*"}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SECRET_KEY'] = "jfdhsfjhdskf"
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .expenses import expenses
    from .project import project

    app.register_blueprint(expenses,url_prefix="/")
    app.register_blueprint(project,url_prefix="/")

    from .models import User, Project, Category, Expense
    create_database(app)



    return app

def create_database(app):
    if not path.exists(DB_NAME):
        db.create_all(app=app)
        print("Created database!")