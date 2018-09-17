import flask
import sqlalchemy
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALchemy_DATABASE_URI'] = 'sqlite:////tmp/ml1.db'
db= SQLAlchemy(app)

class items(db.Model):
    __tablename__ = "items"
    id= db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    start_time = db.Column(db.datetime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return '<Category %r>' % self.name

class user(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    addresses = db.relationship('items', backref='user', lazy=True)
    addresses = db.relationship('bit',backref='user', lazy = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tags= db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))
    tags2 = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('pages', lazy=True))

    def __repr__(self):
        return  '<Category %r>' % self.username

class bid(db.Model):
    __tablename__= "bid"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.float, nullable = False)

    def __repr__(self):
        return  '<Category %r>' %self.price

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('items.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)
tags2 = db.Table('tags2',
    db.Column('tag_id', db.Integer, db.ForeignKey('bid.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)



adam = user(1,'adam','123456')
db.session.add(adam)
hoa = user(2,'hoa','123454')
db.session.add(hoa)
hoang = user(3,'hoang','134d')
db.session.add(hoang)
