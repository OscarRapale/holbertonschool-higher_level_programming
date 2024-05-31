from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home route that returns a welcome message.
    """
    return "Welcome to the flask API!"

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route("/data")
def data():
    """
    Data route that returns all users.
    """
    return jsonify(users)

@app.route("/status")
def status():
    """
    Status route that returns 'OK'.
    """
    return "OK"

@app.route("/user/<username>")
def user(username):
    """
    User route that returns the user with the given username.
    If the user does not exist, it returns a 404 status code.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add User route that accepts POST requests to add a new user.
    The new user's data is expected to be provided in the request body as JSON.
    """
    user = request.get_json()
    users[user["username"]] = user
    return jsonify(user)

if __name__ == "__main__":
    app.run()
