from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return f'{word * num}'


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)