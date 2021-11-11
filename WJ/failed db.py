from flask import Flask

from flask_sqlalchemy import SQLAlchemy


DB_NAME= "projects.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = "tyutyurturu"
app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
db=SQLAlchemy(app)

#create_database(app)

from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))
    name = db.Column(db.String(50), nullable=False)
    appointment = db.Column(db.String(50), nullable=False, default="Project Manager")
    #projects = db.relationship('Project')

class Project(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(50),nullable=False)
    budget = db.Column(db.Float,nullable=False, default=1000000)
    #expenses = db.relationship('Expense')

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


if __name__ == "__main__":
    app.run(debug=True)
