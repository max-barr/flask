# Import flask to allow us to create app, render template allows us to use templates
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/success')
def success():
    return "Success!"

@app.route('/hello/<name>')
def hello(name):
    print(f"Name = {name}")
    return f"Hello, {name}!"

@app.route('/hello/<name>/<int:num>')
def hello_num(name, num):
    return render_template("hello.html", name=name, num=num)

@app.route('/user/<username>/<id>')
def show_user_profile(username, id):
    print(f"username: {username}")
    print(f"id: {id}")
    return "Username: " + username + ", id: " + id

@app.route('/lists')
def render_lists():
    student_info = [
        {'name' : 'Mike', 'age' : 34},
        {'name' : 'Shaq', 'age' : 36},
        {'name' : 'Max', 'age' : 29},
        {'name' : 'Sarah', 'age' : 23},
        {'name' : 'Jackson', 'age' : 28},
    ]
    return render_template('lists.html', random_numbers = [3,1,4,6,34], students = student_info)

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5001)
