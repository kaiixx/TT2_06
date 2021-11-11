class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))
    name = db.Column(db.String(50), nullable=False)
    appointment = db.Column(db.String(50), nullable=False, default="Project Manager")
    projects = db.relationship('Project')