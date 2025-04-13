from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import json

with open('config.json','r') as c:
    params = json.load(c)["params"]


local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'



if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']


else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['proud_uri']

db = SQLAlchemy(app)

class Medicines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(500), nullable=False)
    medicines= db.Column(db.String(500), nullable=False)
    products = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    mid = db.Column(db.String(120), nullable=False)

class Posts(db.Model):
    mid = db.Column(db.Integer, primary_key=True)
    medical_name = db.Column(db.String(80), nullable=False)
    owner_name = db.Column(db.String(200), nullable=False)
    phone_no = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(120), nullable=False)

class Addmp(db.Model):
    sno = db.Column(db.Integer,  primary_key=True)
    medicine = db.Column(db.String, nullable=False)

class Addpd(db.Model):
    sno = db.Column(db.Integer,  primary_key=True)
    product = db.Column(db.String, nullable=False)


class Logs(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.String, nullable=True)
    action = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(100), nullable=False)