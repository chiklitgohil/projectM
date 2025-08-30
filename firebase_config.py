import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Path to your service account key JSON file
cred = credentials.Certificate("projectm-84c11-firebase-adminsdk-fbsvc-bfcbf9e50d.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Add a user
user_ref = db.collection("users").add({
    "name": "John Doe",
    "email": "john@example.com",
    "createdAt": datetime.utcnow()
})

print("User created:", user_ref)

# Add a report linked to user
report_ref = db.collection("reports").add({
    "userId": user_ref[1].id,  # doc ID from user
    "type": "tree_cutting",
    "location": {"lat": 12.34, "lng": 56.78},
    "photoURL": "https://example.com/photo.jpg",
    "createdAt": datetime.utcnow()
})

print("Report created:", report_ref)