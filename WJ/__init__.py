from flask import Flask
from models import Project
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

DB_NAME= "projects.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "tyutyurturu"
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .models import Project
    #create_database(app)

    return app


db.create_all()

Project_1 = Project(id= 1,user_id= 4,name= "RTF",budget= 12000,
            description= "Realtime Face Recogniton")

db.session.add(Project_1)

Project_2 = Project(id= 2,user_id= 1,name= "SWT",budget= 80000,
            description= "Smart Watch Tracker")

db.session.add(Project_2)

Project_3 = Project(id= 3,user_id= 2,name= "ULS",budget= 11000,
            description= "Upgrade Legacy System")

db.session.add(Project_3)

db.session.commit()
