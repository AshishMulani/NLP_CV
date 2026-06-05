# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return ('Hello World')

# @app.route('/hello')
# def hello_index():
#     return ('Welcome to Python Programming')

# if __name__ == '__main__':
#     app.run(debug=True)
    # app.run(debug=True)  we don't have to always stop and re-run the code 
    # instead we can apply changes
    
    
    

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_BLANK():
    return 'Hello BLANK'

@app.route('/admin')
def hello_admin():
    return 'Hello Administrator'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Welcome %s as guest!' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))

if __name__ == '__main__':
    app.run(debug=True)