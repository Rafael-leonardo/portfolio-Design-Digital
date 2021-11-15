from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")

@app.route("/projetos")
def projetos():
    return render_template("projetos.html")

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")

if __name__ == '__main__':
    app.run(port=8000, debug=True)
