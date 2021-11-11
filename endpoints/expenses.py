from flask import Blueprint, request, flash, jsonify
from .models import User, Project, Category, Expense 
from . import db
import json 
from sqlalchemy.sql import func

# - View, Add, Delete, Update expenses

expenses = Blueprint('expenses', __name__)

def expense_serializer(expenses):
    return{
        'expense_id':expenses.id,
        'category_id':expenses.category_id,
        'name':expenses.name,
        'description':expenses.description,
        'amount':expenses.amount
    }


#view all expenses for one proj id

@expenses.route("/all_expenses/<int:project_id>")
def all_expenses(project_id):
    expenses= Expense.query.filter_by(project_id=project_id).all()
    if expenses:
        return jsonify([*map(expense_serializer, expenses)])
    else:
        return jsonify({'404': 'No expenses found'})


#add expense for proj id

@expenses.route("/add_expense", methods=['POST'])
def add_expense():
    data = json.loads(request.data)
    new_expense = Expense(project_id=data['project_id'],category_id=data['category_id'],name=data['name'],description=data['description'],amount=data['amount'],created_by=data['user_id'],updated_by=data['user_id'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'201': 'New expense added successfully'})


# delete expense for proj id

@expenses.route('/delete_expense',methods=['DELETE'])
def delete_expense():
    data = json.loads(request.data)
    tobe_deleted = Expense.query.filter_by(id=data['id']).delete()
    if tobe_deleted:
        db.session.commit()
 
        return jsonify({'204':'Deleted successfully'})
    else:
        return jsonify({'404':'Expense not found'})


# edit expense for proj id

@expenses.route("/edit_expense",methods=['PUT'])
def edit_expense():
    data = json.loads(request.data)
    cur_expense = Expense.query.filter_by(id=data['id']).first()
    if data['project_id']:
        cur_expense.project_id = data['project_id']
    if data['category_id']:
        cur_expense.category_id = data['category_id']
    if data['name']:
        cur_expense.name = data['name']
    if data['description']:
        cur_expense.description = data['description']
    if data['amount']:
        cur_expense.amount = data['amount']
    cur_expense.updated_at = func.now()
    cur_expense.updated_by = data['user_id']
    db.session.commit()

    return jsonify({'204': 'Edited successfully'})
