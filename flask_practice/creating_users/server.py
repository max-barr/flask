from flask import Flask, render_template, request, redirect
#import the class
from user import User

app = Flask(__name__)

# Display all users GET request
@app.route("/users")
def index():
    #call the get all class method to get all users
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

# Create a new user GET request
@app.route("/new_user")
def new_user():
    return render_template("create.html")

# Save new user POST request
@app.route("/create_user", methods=["POST"])
def save_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5001)