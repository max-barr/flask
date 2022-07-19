from flask import Flask, render_template
#import the class
from user import User

app = Flask(__name__)

@app.route("/users")
def index():
    #call the get all class method to get all users
    users = User.get_all()
    print(users)
    return render_template("read.html")

@app.route("/create_user", methods=["POST"])
def save_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.


if __name__ == "__main__"
    app.run(debug=True, host='localhost', port=5001)