from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = "What's innn a name"



if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5001)