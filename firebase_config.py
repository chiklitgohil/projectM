import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key JSON file
cred = credentials.Certificate("D:\dev\code\hackout25\projectM\projectm-84c11-firebase-adminsdk-fbsvc-bfcbf9e50d.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Add data
doc_ref = db.collection("users").document("chiklit")
doc_ref.set({
    "name": "Chiklit Gohil",
    "age": 18,
    "isStudent": True
})

# Read data
doc = db.collection("users").document("chiklit").get()
if doc.exists:
    print("Document data:", doc.to_dict())
else:
    print("No such document!")