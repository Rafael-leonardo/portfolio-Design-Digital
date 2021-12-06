from flask import Flask, render_template, request
from livereload import Server

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
    server = Server(app.wsgi_app)
    app.run()
