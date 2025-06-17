from flask import Flask, Blueprint, request, render_template, session, redirect

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if session:
        return redirect('/')
    else:
    
        if request.method == 'POST':
            session = True
            return redirect('/')
        
        return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():

    if session:
        return redirect('/')
    else:
        return render_template('register.html')

@auth.route('/logout')
def logout():

    session = False

    if session:
        return redirect('/')
    else:
        return redirect('/login')