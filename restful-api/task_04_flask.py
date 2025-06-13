from flask import Flask, jsonify, request
app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API", 200


@app.route('/status')
def status():
    return jsonify({"status": "OK"}), 200

@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys())), 200

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run()
