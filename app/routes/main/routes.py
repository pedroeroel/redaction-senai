from flask import Flask, Blueprint, request, render_template, session, redirect, jsonify

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():

    if session:
        return redirect('/home')
    else:
        return render_template('index.html', session=session)
    
@main.route('/home', methods=['GET'])
def home():

    if session:
        return render_template('home.html', session=session)
    else:
        return redirect('/login')
    
@main.route('/topics', methods=['GET'])
def themes():
    if session:
        return render_template('topics.html')
    else:
        return redirect('/login')
    
@main.route('/topics/<int:topic_id>', methods=['GET'])
def topic_detail(topic_id):
    if session:
        return render_template(f'/topics/{topic_id}.html')
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