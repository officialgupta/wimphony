from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username
        
class SoundEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    user = db.relationship('User',
    backref=db.backref('soundentries', lazy='dynamic'))
    
    location = db.Column(db.String(80))
    strength = db.Column(db.Integer)
    name = db.Column(db.String(80))
    
    def __init__(self, user_id, location, strength, name):
        self.user_id = user_id
        self.location=location
        self.strength=strength
        self.name=name

    def __repr__(self):
        return '<id %r>' % self.id


