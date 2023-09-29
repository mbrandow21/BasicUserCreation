from flask import Flask, jsonify, request, render_template
from user_verification import verify_user
from user_creation import create_user

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if data exists and if it contains required fields
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid request data"}), 400

    username = data['username'].strip()
    password = data['password'].strip()

    if not username:
        return jsonify({"error": "Enter a username"}), 400
    if not password:
        return jsonify({"error": "Enter a password"}), 400

    success = create_user(username, password)
    if success:
        return jsonify({"message": "Registration successful!"}), 201
    else:
        return jsonify({"error": "Registration failed or username already exists"}), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid request data"}), 400

    username = data['username']
    password = data['password']

    is_verified = verify_user(username, password)
    if is_verified:
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"error": "Invalid username or password"}), 400

if __name__ == '__main__':
    app.run(debug=True)
