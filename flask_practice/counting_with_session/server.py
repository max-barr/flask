from flask import Flask, redirect, render_template, session
app = Flask(__name__)
app.secret_key = "Bill can't do it..."

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/reset')
def increment():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5001)