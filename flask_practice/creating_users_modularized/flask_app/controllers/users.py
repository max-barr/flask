from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import User


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

# Show User GET request
@app.route("/users/show/<int:id>")
def show_user(id):
    user = User.get_one(id)
    return render_template("show.html", user = user)

# Edit User GET request
@app.route("/users/edit/<int:id>")
def edit_user(id):
    user = User.get_one(id)
    return render_template("edit.html", user = user)

# Update User POST request
@app.route("/users/update/<int:id>", methods=["POST"])
def update_user(id):
    data = {
        "id" : id,
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.update(data)
    return redirect("/users")

# Delete user POST request
@app.route("/users/destroy/<int:id>")
def destroy(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect("/users")