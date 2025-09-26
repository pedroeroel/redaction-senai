from flask import Flask, Blueprint, request, render_template, session
from ...firebase import *

essay = Blueprint('essay', __name__, template_folder='templates')

@essay.route('/new_essay', methods=['GET', 'POST'])
def new_essay():
    if request.method == 'GET':
        return render_template('new_essay.html')
    elif request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session.get('user_id')  # Assuming user_id is stored in session
        if user_id:
            essay_data = {
                'title': title,
                'content': content
            }
            # Get the current number of essays for the user to determine the next essay_id
            user_essays = get_user_essays(user_id)  # Assumes this function returns a list of essays
            essay_id = len(user_essays) + 1
            add_essay_data(essay_id=essay_id, user_id=user_id, data=essay_data)
            return "Essay added successfully!"
        else:
            return "User not logged in", 401

@essay.route('/my-essays')
def my_essays(): #show user essays
    if request.method == 'GET':
        
        session['user_id'] = 1

        essays = get_all_essays(user_id=session.get('user_id'))

        return render_template('my_essays.html')

@essay.route('/essay_results')
def essay_results():
    if request.method == 'GET':
        return render_template('essay_results.html')