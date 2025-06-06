from flask import Flask, Blueprint, request, render_template, session

main = Blueprint('main', __name__, template_folder='templates')

session = True

@main.route('/')
def index():

    if session:
        return render_template('home.html')
    else:
        return render_template('index.html')    