from flask import Flask, Blueprint, request, render_template, session, redirect

games = Blueprint('games', __name__, template_folder='templates')

@games.route('/games', methods=['GET'])
def games_list():
    if session:
        return render_template('games.html')
    else:
        return redirect('/login')