# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process-task', methods=['POST'])
def process_task():
    # Get the task name from the request
    task_name = request.json.get('name')
    
    # Log the task name to the terminal
    print(f"Task '{task_name}' has been successfully processed by Python.")
    
    # Return a success response
    return jsonify({"message": f"Task '{task_name}' has been successfully processed by Python."})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
