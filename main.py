from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/<string:name>")
def error(name):
    return render_template("error.html", pagina=name)