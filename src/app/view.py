from app import *
from flask import *

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