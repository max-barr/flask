from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", times=3)

@app.route('/play/<x>')
def boxFunction(x):
    return render_template("index.html", times=int(x))

@app.route('/play/<x>/<color>')
def boxColorFunction(x,color):
    return render_template("index.html", times=int(x), color=color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)