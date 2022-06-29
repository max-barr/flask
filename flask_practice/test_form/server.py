from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5001)