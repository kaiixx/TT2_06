from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy
import sqlite3

from security import authenticate, identity
from resources.user import UserRegister
from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)
db = SQLAlchemy(app)

connection = sqlite3.connect('project_expenses.db')
cursor = connection.cursor()

# create users table in sqlite database
query = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username text, password text, name text, appointment text)"
cursor.execute(query)

connection.commit()


@app.before_first_request
def create_tables():
    db.create_all()


user_1 = User(username='user101', password='123456',

              name='Jacky', appointment='Project Lead')
db.session.add(user_1)

user_2 = User(username='user102', password='123456',

              name='Tommy', appointment='Project Manager')
db.session.add(user_2)

user_3 = User(username='user103', password='123456',

              name='Tom', appointment='Project Manager')
db.session.add(user_3)

user_4 = User(username='user104', password='123456',

              name='Helen', appointment='Project Manager')
db.session.add(user_4)

user_5 = User(username='user105', password='123456',

              name='Mark', appointment='Senior Project Manager')
db.session.add(user_5)

db.session.commit()

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
