from . import db
from sqlalchemy.sql import func

class Project(db.model):
    id = db.column(db.Integer(11),primary_key=True)
    user_id = db.column(db.Integer(11),db.ForeignKey('user.id'),nullable=False)
    name = db.column(db.String(50),nullable=False)
    description = db.column(db.String(50),nullable=False)
    budget = db.column(db.Float(50),nullable=False,default=1000000)