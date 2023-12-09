from flask import Flask, render_template, json, request

from routes import calc_options


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.get('/main-menu')
def main_menu():
    return render_template("main-menu.html")

@app.post('/operation')
def operation():
    selected = request.form['operation']
    input = request.form['user-input']
    if selected in calc_options:
        return render_template(selected + ".html", input_user=input)
    return render_template("error.html")
    
