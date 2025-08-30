from flask import Flask, request, jsonify, render_template
import os
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# In-memory storage for demo
reports = []

# Ensure uploads folder exists
os.makedirs("uploads", exist_ok=True)

# 1. Initialize Firebase Admin SDK
cred = credentials.Certificate("projectm-84c11-firebase-adminsdk-fbsvc-bfcbf9e50d.json.json")  # path to your key file
firebase_admin.initialize_app(cred)

# 2. Create Firestore client
db = firestore.client()

# Landing page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user')
def user():
    return render_template('index.html')

# User report page
@app.route('/report_page')
def report_page():
    return render_template('report.html')

# Admin dashboard page
@app.route('/admin')
def admin_page():
    return render_template('dashboard.html')





# 3. Route to handle report submission
@app.route('/submit_report', methods=['POST'])
def submit_report():
    try:
        data = request.json  # Expecting JSON from frontend
        report = {
            "photo_url": data.get("photo_url"),
            "label": data.get("label"),
            "location": data.get("location"),
            "timestamp": firestore.SERVER_TIMESTAMP
        }
        # Store report in Firestore
        db.collection("reports").add(report)

        return jsonify({"status": "success", "message": "Report submitted!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

# Endpoint to get all reports for admin dashboard
@app.route('/get_reports')
def get_reports():
    return jsonify(reports)

# Endpoint to update status or credit
@app.route('/update_report', methods=['POST'])
def update_report():
    idx = int(request.form.get("index"))
    action = request.form.get("action")
    
    if action == "resolve":
        reports[idx]["status"] = "Resolved"
    elif action == "credit":
        reports[idx]["credit"] = "Yes"
    
    return jsonify({"message": "Updated successfully"})

if __name__ == '_main_':
    app.run(debug=True)



   