import os
from flask import Flask, render_template, json, request

from calculator.operations.example import derOperation
from routes import calc_options, Routes
# flask tutorial https://flask.palletsprojects.com/en/stable/tutorial/
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def home():
        return render_template("base.html")

    @app.get("/" + Routes.MAINMENU.value)
    def main_menu():
        return render_template("main-menu.html")

    @app.post("/" + Routes.OPERATION.value)
    def operation():
        selected = request.form['operation']
        input = request.form['user-input']
        if selected in calc_options:
            return render_template(selected + ".html", input_user=input)
        return render_template("error.html")

    @app.post("/" + Routes.DERIVATIVE.value)
    def derivative():
        input = request.form['derivative-input']
        constant = request.form['derivative-constant']
        # here goes the real calculator
        (res, err) = derOperation(input, constant)
        return render_template("result.html", **locals())

    # TODO: create a post for each operation type    
    return app
