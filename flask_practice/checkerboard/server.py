from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", x=8, y=8)

@app.route('/<int:x>')
def board(x):
    return render_template("index.html", x=int(x), y=8)

@app.route('/<int:x>/<int:y>')
def rows(x,y):
    return render_template("index.html", x=int(x), y=int(y))

if __name__=="__main__":
    app.run(debug=True)