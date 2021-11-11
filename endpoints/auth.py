from flask import Blueprint, request, flash, jsonify
from .models import User
from . import db
import json 
from sqlalchemy.sql import func

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['POST'])
def login():
    data = json.loads(request.data)
    
    username = data['username']
    password = data['password']

    user = find_by_username(User, username)
    if user:
        if password == str(user.password):
            return jsonify({'200':'Login success'})

    return jsonify({'400':'Login failed'})

def find_by_username(User, username):
    return User.query.filter_by(username=username).first()