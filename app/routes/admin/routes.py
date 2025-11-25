from flask import Flask, Blueprint, request, render_template, session, redirect
from app.firebase import get_all_users, delete_user, count_users, update_user_data_by_user_id, get_user_data
from app.firebase import get_grade_average, count_essays

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin', methods=['GET'])
def dashboard():
    if session.get('admin') == True:
        
        if request.method == 'GET':
            users = get_all_users()
            user_count = int(count_users())
            essay_count = count_essays()
            essay_avg = get_grade_average() or False
            
            return render_template('dashboard.html', users=users, user_count=user_count, essay_count=essay_count, essay_avg=essay_avg)
        
    else:        
        return redirect('/login')
    
@admin.route('/admin/delete_user/<string:id>')
def remove_user(id):
    if session.get('admin') == True:

            try:
                delete_user(id)
            
            except Exception as e:
                print(e)
                
            finally:
                return redirect('/admin')
            
    else:
        redirect('/login')
        
        
@admin.route('/admin/edit_user/<string:id>', methods=['GET', 'POST'])
def edit_user(id):
    if not session.get('admin'):
        return redirect('/login')

    user = get_user_data(id)
    if not user:
        return redirect('/admin')

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        score = request.form.get('score')
        new_password = request.form.get('password')
        is_admin = True if request.form.get('admin') == "on" else False

        update_data = {
            "username": username,
            "email": email,
            "score": int(score),
            "admin": is_admin
        }

        # Only update password if user typed a new one
        if new_password.strip() != "":
            update_data["password"] = new_password

        update_user_data_by_user_id(id, update_data)

        return redirect('/admin')

    return render_template('edit_user.html', user=user)
