from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = 'keykey123'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5001)