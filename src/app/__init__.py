from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "isso é seguro, confia!"

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')

@app.route('/projetos')
def porotfolio():
    return render_template('portfolio.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')