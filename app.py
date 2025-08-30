from flask import Flask, request, jsonify, render_template
import os
from datetime import datetime

app = Flask(__name__)

# In-memory storage for demo
reports = []

# Ensure uploads folder exists
os.makedirs("uploads", exist_ok=True)

# Landing page
@app.route('/')
def home():
    return render_template('index.html')

# User report page
@app.route('/report_page')
def report_page():
    return render_template('report.html')

# Admin dashboard page
@app.route('/admin')
def admin_page():
    return render_template('admin.html')

# Endpoint to submit a report
@app.route('/report', methods=['POST'])
def report():
    issue_type = request.form.get("issue")
    photo = request.files.get("photo")
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    
    # Save photo if exists
    if photo:
        photo_path = os.path.join("uploads", photo.filename)
        photo.save(photo_path)
    else:
        photo_path = None
    
    report_entry = {
        "issue": issue_type,
        "photo_path": photo_path,
        "lat": lat,
        "lon": lon,
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "status": "Pending",
        "credit": "No"
    }
    
    reports.append(report_entry)
    
    return jsonify({
        "message": "Report submitted successfully!",
        "points": 50 if issue_type=="cutting" else 30  # simple points example
    })

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



   