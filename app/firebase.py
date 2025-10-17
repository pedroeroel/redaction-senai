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

