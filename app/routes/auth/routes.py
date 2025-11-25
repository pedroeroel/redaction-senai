from flask import Flask, Blueprint, request, render_template, session, redirect
from app.firebase import get_score, get_user_by_fields, register_user

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

        try:
            user = get_user_by_fields(email, password)
            
        except Exception as e:
            print(f"Error fetching user: {e}")

        if not user:
            return render_template('login.html', error="Invalid email or password.")
        else:
            session['email'] = user['email']
            session['user_id'] = user['id']
            session['admin'] = user.get('admin', False)
            session['username'] = user['username']      
            session['score'] = get_score(str(session['user_id']))
            
            return redirect('/')


@auth.route('/register', methods=['GET', 'POST'])
def register():

    if session:
        return redirect('/')
    else:

        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            username = request.form.get('username')

            try:
                new_user_id = register_user(email, password, username)
            except Exception as e:
                print(f"Error registering user: {e}")
                return render_template('register.html', error="Registration failed. Please try again.")

            session['email'] = email
            session['user_id'] = str(new_user_id)
            session['admin'] = False
            session['username'] = username
            session['score'] = 0

            return redirect('/')

        return render_template('register.html')

@auth.route('/logout')
def logout():

    session.clear()

    if session:
        print("Error logging out")
        return redirect('/')
    else:
        return redirect('/login')
