from flask import Flask, Blueprint, request, render_template, session, redirect, url_for
import json
import requests
from ...firebase import get_all_essays, add_essay_data, get_essay_data, get_score, update_score, get_example_essays, get_specific_essay

essay = Blueprint('essay', __name__, template_folder='templates')


# -------------------------------
# API CALL
# -------------------------------
def get_essay_analysis(essay_text, title, theme):
    payload = {
        "essay": essay_text,
        "title": title,
        "theme": theme
    }

    try:
        r = requests.post(
            "https://the-learners-dream.vercel.app/api/redaction",
            json=payload
        )
        r.raise_for_status()
        return r.json()

    except Exception as e:
        print(f"[API ERROR] {e}")
        return None



# -------------------------------
# NEW ESSAY
# -------------------------------
@essay.route("/new-essay", methods=["GET", "POST"])
def new_essay():

    user_id = session.get("user_id")
    if not user_id:
        return redirect("/")

    # Score check
    if get_score(user_id) < 100:
        return redirect("/")

    # ---- GET ----
    if request.method == "GET":
        print("LOG: GET /new-essay")
        return render_template("new_essay.html")

    # ---- POST ----
    print("LOG: POST /new-essay")

    original_essay_data = {
        "title": request.form.get("title"),
        "content": request.form.get("text"),
        "theme": request.form.get("theme")
    }

    session["original_essay_data"] = original_essay_data

    analysis = get_essay_analysis(
        original_essay_data["content"],
        original_essay_data["title"],
        original_essay_data["theme"]
    )

    if not analysis:
        print("LOG: API returned nothing → redirecting")
        return redirect("/new-essay")

    session["analysis_results"] = analysis

    # subtract points ONLY after success
    update_score(user_id, -100)

    print(f"LOG: Analysis stored in session for user {user_id}")
    print(analysis)
    return redirect("/essay-results")



# -------------------------------
# MY ESSAYS
# -------------------------------
@essay.route("/my-essays")
def my_essays():

    user_id = session.get("user_id")
    if not user_id:
        return redirect("/new-essay")

    try:
        essays = get_all_essays(user_id)
    except Exception as e:
        print(f"[ERROR] Fetching essays: {e}")
        essays = []

    return render_template("my_essays.html", essays=essays)



# -------------------------------
# VIEW ESSAY
# -------------------------------
@essay.route("/my-essays/<essay_id>")
def view_essay(essay_id):

    user_id = session.get("user_id")
    if not user_id:
        return redirect("/new-essay")

    try:
        essay_data = get_essay_data(str(essay_id), user_id)
        if not essay_data:
            print("LOG: Essay not found → redirect")
            return redirect("/my-essays")
    except Exception as e:
        print(f"[ERROR] {e}")
        return redirect("/my-essays")

    return render_template("view_essay.html", essay=essay_data, essay_id=essay_id)



# -------------------------------
# ESSAY RESULTS PAGE
# -------------------------------
@essay.route("/essay-results")
def essay_results():
    print("LOG: GET /essay-results")

    user_id = session.get("user_id")
    session["score"] = get_score(user_id)

    if "original_essay_data" not in session or "analysis_results" not in session:
        print("SESSION ERROR → redirecting")
        return redirect("/new-essay")

    results = session["analysis_results"]

    return render_template(
        "essay_results.html",
        results=results,
        original=session["original_essay_data"]
    )

# -------------------------------
# SAVE / DISMISS ACTIONS
# -------------------------------
@essay.route("/handle_essay_action", methods=["POST"])
def handle_essay_action():

    action = request.form.get("action")
    user_id = session.get("user_id")

    print(f"LOG: handle_essay_action → {action}")

    if not user_id:
        return redirect("/new-essay")

    session['score'] = get_score(session.get('user_id'))
    # ---------------------
    # DISMISS
    # ---------------------
    if action == "dismiss":
        session.pop("original_essay_data", None)
        session.pop("analysis_results", None)
        return redirect("/my-essays")

    # ---------------------
    # SAVE
    # ---------------------
    if action == "save":

        original = session.get("original_essay_data")
        results = session.get("analysis_results")

        if not original or not results:
            print("SAVE ERROR: Missing session data")
            return redirect("/essay-results")

        try:
            # build essay object
            essay_data = {
                "title": original.get("title"),
                "content": original.get("content"),
                "theme": original.get("theme"),
                "grade": str(results.get("generalGrade")),
                "comments": results.get("comments"),
                "competencies": results.get("competencies")
            }

            # next ID
            user_essays = get_all_essays(user_id)
            new_id = str(len(user_essays) + 1)

            add_essay_data(
                essay_id=new_id,
                user_id=user_id,
                data=essay_data
            )

            # cleanup
            session.pop("original_essay_data", None)
            session.pop("analysis_results", None)

            return redirect("/my-essays")

        except Exception as e:
            print(f"[SAVE ERROR] {e}")
            return redirect("/essay-results")

    # fallback
    return redirect("/my-essays")

@essay.route('/examples')
def examples():
    results = get_example_essays()
    return render_template('examples.html', essays=results)

@essay.route('/examples/<int:id>/<int:index>')
def example(id, index):
    essay_data = get_specific_essay(id, index)
    
    if not essay_data:
        return redirect('/examples')
    
    return render_template('example_essay.html', essay=essay_data)