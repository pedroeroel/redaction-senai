from flask import Flask, Blueprint, request, render_template, session, redirect, url_for
import json
import requests # REQUIRED: For making the external API call
# FIX: Use explicit imports for clarity and to avoid NameError
from ...firebase import get_all_essays, add_essay_data, get_essay_data, get_score, update_score

essay = Blueprint('essay', __name__, template_folder='templates')

# --- Helper Function for API Call ---
def get_essay_analysis(essay_text, title, theme):
    """Calls the external analysis API and returns the JSON results."""
    api_payload = {
        'essay': essay_text,
        'title': title,
        'theme': theme
    }
    
    try:
        api_response = requests.post(
            "https://the-learners-dream.vercel.app/api/redaction",
            json=api_payload
        )
        api_response.raise_for_status()
        return api_response.json()
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Failed to fetch analysis from external API: {e}")
        return None 

# --- FLASK ROUTES ---

@essay.route('/new-essay', methods=['GET', 'POST'])
def new_essay():
    if request.method == 'GET':
        print("LOG: Navigating to GET /new-essay")
        session['user_id'] = '1' 
        return render_template('new_essay.html')

    elif request.method == 'POST':
        print("LOG: Received POST data on /new-essay (initial submission).")
        
        session['user_id'] = session.get('user_id', '1')

        original_essay_data = {
            'title': request.form['title'],
            'content': request.form['text'],
            'theme': request.form['theme']
        }
        # FIX: Store original data in session FIRST
        session['original_essay_data'] = original_essay_data
        
        # 1. Call the external API using the server
        analysis_results = get_essay_analysis(
            original_essay_data['content'],
            original_essay_data['title'],
            original_essay_data['theme']
        )
        
        # 2. Store the analysis results in the session
        if analysis_results:
            session['analysis_results'] = analysis_results
            print("LOG: Server successfully fetched and stored API analysis results in Flask session.")
            update_score(session['user_id'], -100) # Deduct 100 points for analysis
        else:
            # Handle API failure
            return redirect('/new-essay')   
        
        print(f"LOG: Stored original essay data in session for user {session.get('user_id')}.")
        return redirect('/essay-results') 

@essay.route('/my-essays', methods=['GET'])
def my_essays():
    user_id = str(session['user_id'])
    
    if request.method == 'GET':
        print("LOG: Navigating to GET /my-essays.")

        if not user_id:
            print("LOG: User ID missing. Redirecting to /new_essay.")
            return redirect('/new-essay') 

        try:
            essays = get_all_essays(user_id=user_id)
            print(f"LOG: Successfully fetched {len(essays)} essays for user {user_id}.")
        except Exception as error:
            print(f"ERROR: Error fetching essays: {error}")
            essays = []

        return render_template('my_essays.html', essays=essays)

@essay.route('/my-essays/<essay_id>')
def view_essay(essay_id):
    session['user_id'] = session.get('user_id', '1')
    user_id = session.get('user_id')

    if not user_id:
        print("LOG: User ID missing. Redirecting to /new_essay.")
        return redirect('/new-essay') 

    try:
        essay_data = get_essay_data(essay_id=str(essay_id), user_id=user_id)
        if essay_data:
            print(f"LOG: Successfully fetched essay ID {essay_id} for user {user_id}.")
        else:
            print(f"LOG: Essay ID {essay_id} not found for user {user_id}. Redirecting to /my-essays.")
            return redirect('/my-essays')
    except Exception as error:
        print(f"ERROR: Error fetching essay ID {essay_id}: {error}")
        return redirect('/my-essays')
    
    return render_template('view_essay.html', essay=essay_data, essay_id=essay_id)

@essay.route('/essay-results')
def essay_results():
    print("LOG: Navigating to GET /essay-results (Performance page).")
    
    session['user_id'] = session.get('user_id', '1')
    session['score'] = get_score(session['user_id'])
    
    # FIX: Enforce session integrity before showing the results page
    if 'original_essay_data' not in session or 'analysis_results' not in session:
        print("ERROR: Session data missing. Redirecting to start.")
        return redirect('/new-essay') 

    analysis_results_json = json.dumps(session['analysis_results'])
    
    # Pass the JSON string directly to the template
    return render_template('essay_results.html', session=session, analysis_results_json=analysis_results_json)

@essay.route('/handle_essay_action', methods=['POST'])
def handle_essay_action():

    action = request.form.get('action')
    user_id = session.get('user_id') 
    
    print(f"LOG: Received POST on /handle_essay_action. Action: '{action}'")

    if not user_id:
        print("LOG: User ID missing. Redirecting to /new_essay.")
        return redirect('/new-essay') 
        
    # --- DISMISS ACTION ---
    if action == 'dismiss':
        session.pop('original_essay_data', None)
        session.pop('analysis_results', None)
        print(f"LOG: DISMISS action performed. Cleared essay data from session.")
        return redirect('/my-essays') 

    # --- SAVE ACTION ---
    if action == 'save':
        original_data = session.get('original_essay_data')
        results = session.get('analysis_results') 
        
        if not original_data or not results:
            print("ERROR: SAVE action failed. Original essay or analysis data missing from session.")
            return redirect('/essay-results')

        try:
            raw_grade = results.get('generalGrade')
            print(f"LOG: Analysis data found. Grade: {raw_grade}")

            # AGGREGATE ALL DATA POINTS
            essay_data = {
                'title': original_data.get('title', 'Redação Sem Título'),
                'content': original_data.get('content', 'Conteúdo indisponível.'), 
                'theme': original_data.get('theme', 'Tema Indefinido'),
                
                # FIX: Cast grade to string (Firebase is expecting a str)
                'grade': str(raw_grade) if raw_grade is not None else 'N/A', 
                
                'comments': results.get('comments'),
                'competencies': results.get('competencies')
            }
            
            # 1. Determine next ID
            user_essays = get_all_essays(user_id) 
            essay_id = len(user_essays) + 1
            
            # 2. FIX: Cast essay_id to string (Firestore document ID must be a str)
            essay_id_str = str(essay_id) 
            
            # Save to database 
            add_essay_data(essay_id=essay_id_str, user_id=user_id, data=essay_data)
            
            # SUCCESS! Now, explicitly remove the data from the session
            session.pop('original_essay_data', None)
            session.pop('analysis_results', None)
            
            print(f"LOG: SAVE SUCCESSFUL. Essay ID {essay_id_str} saved for user {user_id}. Session cleared.")
            return redirect('/my-essays') 

        except Exception as e:
            # This catch now traps any error in the get_all_essays/add_essay_data flow
            print(f"ERROR: Database or data aggregation error during SAVE: {e}")
            return redirect('/essay-results')
    
    print("LOG: Unrecognized action received. Defaulting redirect to /my-essays.")
    return redirect('/my-essays')