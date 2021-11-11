from flask import Blueprint, request, flash, jsonify
from flask_jwt import JWT, jwt_required, current_identity
from .models import Project
from . import db
import json 
from sqlalchemy.sql import func

# - View all projects under certain user 

projects = Blueprint('projects', __name__)

def projects_serializer(projects):
    return{
        'id':projects.id,
        'name':projects.name,
        'description':projects.description,
        'budget':projects.budget,
        'expenses':projects.expenses
        }

@app.route("/view_projects/<int:user_id>)
def all_projects(user_id):
    projects= Project.query.filter_by(user_id=user_id).all()
    if projects:
        return jsonify([*map(projects_serializer, projects)])
    else:
        return jsonify({'404': 'No projects found'})


if __name__ == "__main__":
    app.run(debug=True)