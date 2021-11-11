from flask import Blueprint, request, flash, jsonify
from flask_jwt import JWT, jwt_required, current_identity
from .models import User, Project, Category, Expense 
from . import db
import json 
from sqlalchemy.sql import func

# - View projects
project = Blueprint('project', __name__)

def projects_serializer(projects):
    return{
        'id':projects.id,
        'name':projects.name,
        'description':projects.description,
        'budget':projects.budget,
        }

@jwt_required()
@project.route("/view_projects/<int:user_id>")
def all_projects(user_id):
    projects= Project.query.filter_by(user_id=user_id).all()
    if projects:
        return jsonify([*map(projects_serializer, projects)])
    else:
        return jsonify({'404': 'No projects found'})