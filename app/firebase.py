import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os
import sys
import json
from google.cloud.firestore_v1 import FieldFilter

load_dotenv()

key_source = None
local_path = 'instance/serviceAccountKey.json'
env_var_name = 'FIREBASE_SERVICE_KEY'

if os.path.exists(local_path):
    key_source = local_path
else:
    key_source = os.getenv(env_var_name)
    
if not key_source:
    sys.exit('Firebase service account key not found in local path or environment variable.')

if not firebase_admin._apps:
    if key_source.startswith('{'):
        try:
            cert_dict = json.loads(key_source)
            cred = credentials.Certificate(cert_dict)
        except json.JSONDecodeError:
            sys.exit('Error: FIREBASE_SERVICE_KEY is malformed JSON.')
    else:
        cred = credentials.Certificate(key_source)

    firebase_admin.initialize_app(cred)

db = firestore.client()

def _get_user_snapshot_by_user_id(user_id):
    user_id = str(user_id)
    users_ref = db.collection('register')

    query = users_ref.where(
        filter=FieldFilter('id', '==', user_id)
    ).limit(1).stream()

    for doc in query:
        return doc

    return None

def _get_user_doc_ref_by_user_id(user_id):
    snap = _get_user_snapshot_by_user_id(user_id)
    return snap.reference if snap else None

def get_user_data(user_id):
    user_id = str(user_id)
    users_ref = db.collection('register')

    query = users_ref.where(
        filter=FieldFilter('id', '==', user_id)
    ).limit(1).stream()

    for doc in query:
        data = doc.to_dict()
        data["doc_id"] = doc.id
        return data

    return None

def update_user_data_by_user_id(user_id, update_data):
    doc_ref = _get_user_doc_ref_by_user_id(user_id)
    
    if not doc_ref:
        return False
    
    current = doc_ref.get().to_dict()
    current.update(update_data)
    doc_ref.set(current)

    return True

def get_user_by_fields(email, password):
    users_ref = db.collection('register')
    try:
        for doc in (
            users_ref
                .where(filter=FieldFilter('email', '==', email))
                .where(filter=FieldFilter('password', '==', password))
                .limit(1)
                .stream()
        ):
            print(doc.to_dict())
            return doc.to_dict( )
    except Exception as e:
        print(f"Error querying user by fields: {e}")
    return False

def register_user(email, password, username):
    users_ref = db.collection('register')
    new_user_ref = users_ref.document()
    new_user_id = count_users() + 1
    new_user_ref.set({
        'email': email,
        'password': password,
        'username': username,
        'score': 0,
        'id': str(new_user_id)
    })

    return new_user_id

def get_all_users():
    users_ref = db.collection('register')
    docs = users_ref.stream()
    users = []
    for doc in docs:
        users.append(doc.to_dict())
    return users

def delete_user(user_id):
    doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if doc_ref:
        doc_ref.delete()
        return True
    return False

def count_users():
    users_ref = db.collection('register')
    docs = users_ref.stream()
    count = sum(1 for _ in docs)
    return int(count)

def count_essays():
    count = 0
    for user in db.collection('register').stream():
        for _ in db.collection('register').document(user.id).collection('essays').stream():
            count += 1
    return count

def get_grade_average():
    users_ref = db.collection('register')

    total_grade = 0
    total_essays = 0

    for user in users_ref.stream():
        essay_ref = users_ref.document(user.id).collection('essays')

        for essay in essay_ref.stream():
            data = essay.to_dict()
            grade = data.get("grade")

            if grade is not None:
                total_grade += float(grade)
                total_essays += 1

    if total_essays == 0:
        return 0

    return total_grade / total_essays
    
def add_user_data(user_id, data):
    doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if doc_ref:
        doc_ref.set(data)
        return True
    return False

# --- Essay Register and Fetching ---

def get_essay_data(essay_id, user_id):
    user_doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if not user_doc_ref:
        return None
    doc_ref = user_doc_ref.collection('essays').document(str(essay_id))
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None
    
def add_essay_data(essay_id, user_id, data):
    user_doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if not user_doc_ref:
        return False
    doc_ref = user_doc_ref.collection('essays').document(str(essay_id))
    doc_ref.set(data)
    return True

def update_essay_data(essay_id, user_id, data):
    user_doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if not user_doc_ref:
        return False
    doc_ref = user_doc_ref.collection('essays').document(str(essay_id))
    doc_ref.update(data)
    return True

def delete_essay_data(essay_id, user_id):
    user_doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if not user_doc_ref:
        return False
    doc_ref = user_doc_ref.collection('essays').document(str(essay_id))
    doc_ref.delete()
    return True

def get_all_essays(user_id):
    user_doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if not user_doc_ref:
        return []

    essays = []
    for doc in user_doc_ref.collection('essays').stream():
        essay = doc.to_dict()
        essay['id'] = doc.id
        essays.append(essay)

    print(essays)
    return essays

def get_score(user_id):
    user = get_user_data(user_id)
    try:
        return int(user.get("score", 0)) if user else -1
    except:
        print('error fetching score')
        return 0

def update_score(user_id, points):
    doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if not doc_ref:
        print(f"No user found with id {user_id}")
        return False

    current_score = get_score(str(user_id))

    try:
        print(f"Current score for user {user_id}: {current_score}, updating...")
        new_score = current_score + points
        doc_ref.update({'score': new_score})
    except Exception as e:
        print(f"Error updating score for user {user_id}: {e}")
        return False

    print(f"Score updated for user {user_id}: {current_score} -> {new_score}")
    return True

def get_classes_by_user(user_id):
    user_doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if not user_doc_ref:
        return []

    classes = []
    for doc in user_doc_ref.collection('classes').stream():
        cls = doc.to_dict()
        cls['id'] = doc.id
        classes.append(cls)
    return classes

def get_all_classes():
    classes_ref = db.collection('classes')

    classes = []
    for doc in classes_ref.stream():
        cls = doc.to_dict()
        cls['id'] = doc.id
        classes.append(cls)
    return classes

def add_class_to_user(user_id, class_id, class_data):
    user_doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if not user_doc_ref:
        return False

    doc_ref = user_doc_ref.collection('classes').document(str(class_id))
    doc_ref.set(class_data)
    print(f"Class {class_id} added to user {user_id}.")
    return True

def get_class_content(class_id):
    doc_ref = db.collection('classes').document(str(class_id))
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None
    
def register_class(class_data):
    try:
        classes_ref = db.collection('classes')
        new_class_ref = classes_ref.document()
        class_data['id'] = new_class_ref.id
        new_class_ref.set(class_data)
        print(f"Class '{class_data['title']}' registered with ID: {new_class_ref.id}")
        return True
    except Exception as e:
        print(f"Error registering class '{class_data.get('title', 'N/A')}': {e}")
        return False

def get_example_essays(min_grade=900):
    """
    Returns all essays with generalGrade >= min_grade (default = 900)
    """

    chosen_essays = []

    try:
        users_ref = db.collection("register")
        users = users_ref.stream()

        for user in users:
            user_data = user.to_dict()

            # ensure user doc exists
            if not user_data:
                continue

            # Which one is your TRUE uid?
            # Many of your functions use 'user_id' stored inside the doc
            uid = user_data.get("user_id") or user.id

            user_doc = _get_user_doc_ref_by_user_id(uid)

            if not user_doc:
                print(f"⚠ WARNING: user_doc not found for uid={uid}")
                continue

            essays_ref = user_doc.collection("essays")
            essays = essays_ref.stream()

            for index, essay in enumerate(essays):
                essay_data = essay.to_dict()

                if not essay_data:
                    continue

                grade = essay_data.get("generalGrade", 0)
                if grade < min_grade:
                    continue

                username = user_data.get("username", "Usuário")

                chosen_essays.append({
                    "user_id": uid,
                    "index": index,
                    "username": username,
                    "essay": {
                        "title": essay_data.get("title", "Sem título"),
                        "theme": essay_data.get("theme", "Indefinido"),
                        "content": essay_data.get("content", ""),
                        "generalGrade": grade,
                        "competencies": essay_data.get("competencies", []),
                        "comments": essay_data.get("comments", [])
                    }
                })

        return chosen_essays

    except Exception as e:
        print("❌ Error fetching example essays:", e)
        return []


def get_specific_essay(user_id, index):
    """
    Returns a specific essay for a given user_id and index.
    """
    user_doc_ref = _get_user_doc_ref_by_user_id(user_id)
    if not user_doc_ref:
        return None

    essays_ref = user_doc_ref.collection('essays')
    essays = essays_ref.stream()

    for i, essay in enumerate(essays):
        if i == index:
            return essay.to_dict()

    return None
