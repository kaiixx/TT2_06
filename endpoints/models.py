from . import db
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))
    name = db.Column(db.String(50), nullable=False)
    appointment = db.Column(db.String(50), nullable=False, default="Project Manager")
    projects = db.relationship('Project')


class Project(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(50),nullable=False)
    budget = db.Column(db.Float,nullable=False, default=1000000)
    expenses = db.relationship('Expense')

class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    expenses = db.relationship('Expense')

class Expense(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer(), db.ForeignKey('project.id'), nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    amount= db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    created_by = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_by = db.Column(db.String(50), nullable=False)

