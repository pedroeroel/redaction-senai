from flask import Flask, Blueprint, request, render_template, session, redirect

main = Blueprint('main', __name__, template_folder='templates')

session = True

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
    
@main.route('/subjects', methods=['GET'])
def themes():
    if session:
        return render_template('subjects.html')
    else:
        return redirect('/login')
    
@main.route('/arguments', methods=['GET'])
def arguments():
    if session:
        return render_template('arguments.html')
    else:
        return redirect('/login')
    
@main.route('/examples', methods=['GET'])
def examples():
    if session:
        return render_template('examples.html')
    else:
        return redirect('/login')