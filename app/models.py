from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    activities = db.relationship('Activity', backref='user', lazy=True)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duração em minutos
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
