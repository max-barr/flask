from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users')
def pass_users():
    users = [
        {'first_name' : 'Mike' , 'last_name' : 'Trout'},
        {'first_name' : 'Damian', 'last_name' : 'Lillard'},
        {'first_name' : 'Wayne', 'last_name' : 'Tinkle'},
        {'first_name' : 'Patrick', 'last_name' : 'Mahomes'}
    ]
    return render_template('table.html', users=users)


if __name__=="__main__":
    app.run(debug=True, host='localhost', port=5001)