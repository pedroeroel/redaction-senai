from flask import Flask, Blueprint, request, render_template, session, redirect

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():

    if  session:
        return redirect('/home')
    else:
        return render_template('index.html')
    
@main.route('/home', methods=['GET'])
def home():

    if session:
        return render_template('home.html')
    else:
        return redirect('/login')