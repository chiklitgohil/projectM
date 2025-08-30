from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime
import os
from firebase_config import db  # import Firestore client

app = Flask(__name__)
os.makedirs("uploads", exist_ok=True)

app = Flask(__name__)
os.makedirs("uploads", exist_ok=True)  # ensure upload folder exists

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Report form
@app.route('/report')
def report():
    return render_template("report.html")

# Handle form submission

@app.route('/submit', methods=['POST'])
def submit():
    photo = request.files.get("photo")
    report_type = request.form.get("type")
    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")

    if photo:
        filename = datetime.now().strftime("%Y%m%d%H%M%S_") + photo.filename
        filepath = os.path.join("uploads", filename)
        photo.save(filepath)

    # Prepare report data
    report_data = {
        "type": report_type,
        "latitude": latitude,
        "longitude": longitude,
        "photo_filename": filename if photo else None,
        "timestamp": datetime.now()
    }

    # Add to Firestore collection called "reports"
    db.collection("reports").add(report_data)

    return "Report submitted successfully!"



if __name__ == "__main__":
    app.run(debug=True)
