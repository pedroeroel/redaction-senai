import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os
import sys
import json

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

def get_user_data(user_id):
    user_id = str(user_id)
    doc_ref = db.collection('register').document(user_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

def get_user_by_fields(email, password):
    users_ref = db.collection('register')
    query = users_ref.where('email', '==', email).where('password', '==', password).limit(1)
    results = query.stream()
    for doc in results:
        return doc.to_dict()
    return None
    
def register_user(email, password, username):
    users_ref = db.collection('register')
    new_user_ref = users_ref.document()
    new_user_id = count_users() + 1
    new_user_ref.set({
        'email': email,
        'password': password,
        'username': username,
        'score': 0,
        'id': int(new_user_id)
    })


    return new_user_id

def count_users():
    users_ref = db.collection('register')
    docs = users_ref.stream()
    count = sum(1 for _ in docs)
    return int(count)

def add_user_data(user_id, data):
    user_id = str(user_id)
    doc_ref = db.collection('register').document(user_id)
    doc_ref.set(data)

# --- Essay Register and Fetching ---

def get_essay_data(essay_id, user_id):
    user_id = str(user_id)
    essay_id = str(essay_id)
    # essay_id and user_id MUST be strings
    doc_ref = db.collection('register').document(user_id).collection('essays').document(essay_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    
def add_essay_data(essay_id, user_id, data):
    user_id = str(user_id)
    essay_id = str(essay_id)
    # essay_id and user_id MUST be strings
    doc_ref = db.collection('register').document(user_id).collection('essays').document(essay_id)
    doc_ref.set(data)

def update_essay_data(essay_id, user_id, data):
    user_id = str(user_id)
    essay_id = str(essay_id)
    # essay_id and user_id MUST be strings
    doc_ref = db.collection('register').document(user_id).collection('essays').document(essay_id)
    doc_ref.update(data)

def delete_essay_data(essay_id, user_id):
    user_id = str(user_id)
    essay_id = str(essay_id)
    # essay_id and user_id MUST be strings
    doc_ref = db.collection('register').document(user_id).collection('essays').document(essay_id)
    doc_ref.delete()

def get_all_essays(user_id):
    user_id = str(user_id)
    # user_id MUST be a string
    essays_ref = db.collection('register').document(user_id).collection('essays')
    docs = essays_ref.stream()
    essays = []
    for doc in docs:
        essay = doc.to_dict()
        essay['id'] = doc.id
        essays.append(essay)
    # The printed empty list "[]" in your logs comes from this line, indicating no essays yet.
    print(essays) 
    return essays

def get_score(user_id):
    doc_ref = db.collection('register').document(str(user_id))
    doc = doc_ref.get()
    if doc.exists:
        user_data = doc.to_dict()
        return user_data.get('score', 0)  # Return score or 0 if not found
    else:
        return 0

def update_score(user_id, points):
    doc_ref = db.collection('register').document(str(user_id))
    current_score = get_score(str(user_id))

    try:
        print(f"Current score for user {user_id}: {current_score}, updating...")
        new_score = current_score + points
        doc_ref.update({'score': new_score})
    except Exception as e:
        print(f"Error updating score for user {user_id}: {e}")

    finally:
        print(f"Score updated for user {user_id}: {current_score} -> {new_score}")

    return

def get_classes_by_user(user_id):
    user_id = str(user_id)
    doc_ref = db.collection('register').document(user_id).collection('classes')
    docs = doc_ref.stream()
    classes = []
    for doc in docs:
        class_data = doc.to_dict()
        class_data['id'] = doc.id
        classes.append(class_data)
    return classes

def get_all_classes():
    classes_ref = db.collection('classes')
    docs = classes_ref.stream()
    classes = []
    for doc in docs:
        class_data = doc.to_dict()
        class_data['id'] = doc.id
        classes.append(class_data)
    return classes

def add_class_to_user(user_id, class_id, class_data):
    user_id = str(user_id)
    class_id = str(class_id)
    doc_ref = db.collection('register').document(user_id).collection('classes').document(class_id)
    doc_ref.set(class_data)
    return print(f"Class {class_id} added to user {user_id}.")

def get_class_content(class_id):
    class_id = str(class_id)
    doc_ref = db.collection('classes').document(class_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    
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