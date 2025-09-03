from flask import Flask, render_template, request, redirect, url_for, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# simple in-memory storage
reports = []
credits = 50

@app.route('/')
def home():
    return redirect(url_for('reporter'))

@app.route('/reporter')
def reporter():
    return render_template('reporter.html', credits=credits)

@app.route('/authority')
def authority():
    return render_template('authority.html', reports=reports)

@app.route('/submit_issue', methods=['POST'])
def submit_issue():
    global reports
    issue = request.form['issue']
    lat = request.form['latitude']
    lng = request.form['longitude']
    photo = request.files['photo']

    photo_path = None
    if photo:
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
        photo.save(photo_path)

    reports.append({
        "issue": issue,
        "latitude": lat,
        "longitude": lng,
        "photo": photo.filename
    })

    return redirect(url_for('reporter'))

@app.route('/grant_credits', methods=['POST'])
def grant_credits():
    global credits
    credits += 10  # add 10 credits for testing
    return jsonify({"credits": credits})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)