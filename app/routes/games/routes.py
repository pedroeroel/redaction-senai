from flask import Flask, Blueprint, request, render_template, session, redirect
from app.firebase import get_score, update_score

games = Blueprint('games', __name__, template_folder='templates')

@games.route('/games', methods=['GET'])
def games_list():
    if session:

        session['score'] = get_score(session.get('user_id'))

        return render_template('games.html', score=session['score'])
    else:
        return redirect('/login')
    
@games.route('/games/<int:id>', methods=['GET'])
def games_page(id):
    if session:
        return render_template(f'games/game_{id}.html')
    else:
        return redirect('/login')
    
@games.route('/points/redeem', methods=['POST'])
def redeem_points():
    if not session:
        return redirect('/login')
    
    user_id = session.get('user_id')
    points_to_redeem = int(request.form.get('points', 0))
    
    if points_to_redeem <= 0:
        return "Invalid points to redeem.", 400

    update_score(user_id, points_to_redeem)

    return redirect('/games')