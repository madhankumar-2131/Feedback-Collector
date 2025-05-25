from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
feedback_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['GET'])
def get_feedback():
    return jsonify({"feedbacks": feedback_list})

@app.route('/submit', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    feedback_text = data.get("feedback")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"text": feedback_text, "time": timestamp}
    feedback_list.append(entry)
    return jsonify({"success": True, "entry": entry})

if __name__ == '__main__':
    app.run(debug=True)
