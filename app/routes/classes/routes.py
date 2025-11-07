from flask import Blueprint, render_template, session, redirect
from ...firebase import get_classes_by_user, get_class_content, get_all_classes, register_class

classes = Blueprint('classes', __name__, template_folder='templates')

@classes.route('/interactive-classes', methods=['GET'])
def interactive_classes():
    if not session:
        return redirect('/login')

    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')

    user_classes = get_classes_by_user(user_id)
    all_classes = get_all_classes()
    
    print(f"User {user_id} classes: {user_classes}")
    print(f"All classes: {all_classes}")

    formatted_classes = []
    for c in all_classes:
        formatted_classes.append({
            "id": c.get("id"),
            "title": c.get("title"),
            "description": c.get("description", "Sem descrição disponível."),
            "duration": c.get("duration", "N/A"),
            "status": c.get("status", "pending"),
            "category": c.get("category", "Redação"),
            "level": c.get("level", "Básico"),
            "thumbnail": c.get("thumbnail", "https://example.com/default.png"),
            "link": f"/interactive-classes/{c.get('id')}"
        })

    return render_template('classes.html', classes=formatted_classes)


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
