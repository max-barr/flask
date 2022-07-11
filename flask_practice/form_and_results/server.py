from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "What's innn a name"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def store_info():
    print("Got post info")
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['food'] = request.form['food']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def show_results():
    return render_template('results.html')


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5001)