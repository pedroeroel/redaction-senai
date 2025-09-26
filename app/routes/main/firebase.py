import firebase_admin
from firebase_admin import credentials
import dotenv

serviceAccountKey = dotenv.get_key('.env', 'serviceAccountKey')

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
    doc_ref = db.collection('essays').document(essay_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None