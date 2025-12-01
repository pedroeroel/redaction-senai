from flask import Blueprint, render_template, session, redirect
from ...firebase import get_classes_by_user, get_class_content, get_all_classes, mark_class_as_done, get_score, update_score, get_completed_classes
from flask import request, jsonify

classes = Blueprint('classes', __name__, template_folder='templates')

@classes.route('/interactive-classes', methods=['GET'])
def interactive_classes():
    if not session:
        return redirect('/login')

    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')

    completed_class_ids = get_completed_classes(user_id)
    all_classes = get_all_classes()
    
    print(f"Completed classes for user {user_id}: {completed_class_ids}")
    print(f"All classes: {all_classes}")

    formatted_classes = []
    for c in all_classes:
        status = "completed" if c.get("id") in completed_class_ids else "pending"
        formatted_classes.append({
            "id": c.get("id"),
            "title": c.get("title"),
            "description": c.get("description", "Sem descrição disponível."),
            "duration": c.get("duration", "N/A"),
            "status": status,
            "category": c.get("category", "Redação"),
            "level": c.get("level", "Básico"),
            "thumbnail": c.get("thumbnail", "https://example.com/default.png"),
            "link": f"/interactive-classes/{c.get('id')}"
        })

    session['score'] = get_score(user_id)

    return render_template('classes.html', classes=formatted_classes, session=session)


@classes.route('/interactive-classes/<string:class_id>', methods=['GET'])
def interactive_class(class_id):
    if not session:
        return redirect('/login')

    class_content = get_class_content(class_id)
    print(f"Fetched class content for class {class_id}: {class_content}")
    
    if not class_content:
        return "Class not found", 404

    # ✅ Correct indentation starts here
    formatted_content = {
        "id": class_content.get("id"),
        "title": class_content.get("title"),
        "description": class_content.get("description"),
        "duration": class_content.get("duration"),
        "points": class_content.get("points"),
        "status": class_content.get("status"),
        "category": class_content.get("category"),
        "level": class_content.get("level"),
        "thumbnail": class_content.get("thumbnail", ""),
        "topics": []
    }

    topics = class_content.get("topics", [])
    for topic in topics:
        topic_dict = {
            "title": topic.get("title"),
            "paragraphs": topic.get("content", {}).get("paragraphs", []),
            "tip": topic.get("content", {}).get("tip"),
            "list_items": topic.get("content", {}).get("list_items", []),
            "question": topic.get("content", {}).get("question"),
            "options": topic.get("content", {}).get("options"),
            "correct_answer": topic.get("content", {}).get("correct_answer"),
            "correct_feedback": topic.get("content", {}).get("correct_feedback"),
            "wrong_feedback": topic.get("content", {}).get("wrong_feedback"),
            "materials": topic.get("content", {}).get("materials", []),
            "challenge": topic.get("content", {}).get("challenge"),
        }
        formatted_content["topics"].append(topic_dict)

    print(f"Formatted class content for rendering: {formatted_content}")

    return render_template('class.html', class_content=formatted_content)

@classes.route('/interactive-classes/redeem', methods=['POST'])
def redeem_points():
    # local imports so we don't need to modify top-of-file imports

    if not session:
        return jsonify({"error": "Not authenticated"}), 401

    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    try:
        points_to_redeem = int(request.form.get('points', 0))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid points value"}), 400

    if points_to_redeem <= 0:
        return jsonify({"error": "Invalid points to redeem"}), 400

    try:
        result = update_score(user_id, points_to_redeem)
    except Exception as e:
        return jsonify({"error": "Failed to redeem points", "detail": str(e)}), 500

    if result is False or result is None:
        return jsonify({"error": "Redeem operation failed"}), 500

    return jsonify({"message": "Points redeemed", "user_id": user_id, "points_redeemed": points_to_redeem}), 200

@classes.route('/interactive-classes/mark-done/<string:class_id>', methods=['POST'])
def mark_class_done(class_id):
    if not session:
        return jsonify({"error": "Not authenticated"}), 401

    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    try:
        # Assuming there's a function to update the user's class status
        result = mark_class_as_done(user_id, class_id)
    except Exception as e:
        return jsonify({"error": "Failed to mark class as done", "detail": str(e)}), 500

    if result is False or result is None:
        return jsonify({"error": "Failed to update class status"}), 500

    return jsonify({"message": "Class marked as done", "user_id": user_id, "class_id": class_id}), 200