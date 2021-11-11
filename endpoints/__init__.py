from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy()
DB_NAME="project_expenses.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "jfdhsfjhdskf"
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .models import User, Project, Category, Expense
    create_database(app)


    return app

def create_database(app):
    if not path.exists('database/'+ DB_NAME):
        db.create_all(app=app)
        print("Created database!")