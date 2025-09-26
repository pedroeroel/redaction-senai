import firebase_admin
from firebase_admin import credentials, firestore
import dotenv

try:
    serviceAccountKey = dotenv.get_key('.env', 'serviceAccountKey')
except Exception:
    serviceAccountKey = '../instance/serviceAccountKey.json'

cred = credentials.Certificate(serviceAccountKey)
firebase_admin.initialize_app(cred)

db = firebase_admin.firestore.client()

def get_user_data(user_id):
    doc_ref = db.collection('register').document(user_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    
def add_user_data(user_id, data):
    doc_ref = db.collection('register').document(user_id)
    doc_ref.set(data)

# essay register and fetching

def get_essay_data(essay_id, user_id):
    doc_ref = db.collection('register').document(user_id).collection('essays').document(essay_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    
def add_essay_data(essay_id, user_id, data):
    doc_ref = db.collection('register').document(user_id).collection('essays').document(essay_id)
    doc_ref.set(data)

def update_essay_data(essay_id, user_id, data):
    doc_ref = db.collection('register').document(user_id).collection('essays').document(essay_id)
    doc_ref.update(data)

def delete_essay_data(essay_id, user_id):
    doc_ref = db.collection('register').document(user_id).collection('essays').document(essay_id)
    doc_ref.delete()

def get_all_essays(user_id):
    essays_ref = db.collection('register').document(user_id).collection('essays')
    docs = essays_ref.stream()
    essays = []
    for doc in docs:
        essay = doc.to_dict()
        essay['id'] = doc.id
        essays.append(essay)
    return essays