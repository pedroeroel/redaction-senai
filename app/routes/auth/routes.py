from flask import Flask, Blueprint, request, render_template, session, redirect

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'GET':
        if session:
            return redirect('/')
        else:  
            return render_template('login.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email == "adm@adm" and password == "admin123":
            session['user'] = email
            return redirect('/')

@auth.route('/register', methods=['GET', 'POST'])
def register():

    if session:
        return redirect('/')
    else:
        return render_template('register.html')

@auth.route('/logout')
def logout():

    session.clear()

    if session:
        print("Error logging out")
        return redirect('/')
    else:
        return redirect('/login')
