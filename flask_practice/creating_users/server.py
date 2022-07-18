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


if __name__ == "__main__"
    app.run(debug=True, host='localhost', port=5001)