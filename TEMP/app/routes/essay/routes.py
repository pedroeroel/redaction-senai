from flask import Flask, Blueprint, request, render_template, session

essay = Blueprint('essay', __name__, template_folder='templates')

session = True

@essay.route('/new_essay', methods=['GET', 'POST'])
def new_essay():
    return render_template('new_essay.html')

@essay.route('/essay_results')
def essay_results():
    if request.method == 'GET':
        return render_template('essay_results.html')