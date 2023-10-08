from flask import Flask, url_for, request, send_file, redirect, abort

import random as r

app = Flask(__name__)
user_name = 'Taya'

@app.route('/')
def hello_world():
    c = 25**2
    return f'Hello World!{c}'


@app.route('/horoskop/')
def hello_world2():
    list = ['Today you have a good day', 'Unpleasant events are awaited', 'Good news are waiting for you!']
    return r.choice(list)


@app.route('/login/')
def send_login():
    return send_file("templates/login.html")


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return f'Request method POST - user name = {user}'
    else:
        user = request.args.get('name')
        return f'Request method GET - user name = {user}'



@app.route('/url_for_test/')
def url_for_test():
    return url_for('hello')


# @app.route('/redirect-to-login-page')
# def redirected():
#     return redirect(url_for('login'))


@app.route('/redirect-to-login-page')
def redirected():
    if user_name == 'Admin':
        abort(401)
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))


def this_is_never_execute():
    pass


@app.route('/aborted-page')
def aborted_page():
    abort(401)
    this_is_never_execute()


@app.errorhandler(404)
def page_not_found(error):
    return 'this page does not exist', 404

@app.errorhandler(401)
def unauthorized_user(error):
    return 'you are unauthorized user', 401










with app.test_request_context():
    print(url_for('hello_world2'))
    print(url_for('login'))
    print(url_for('url_for_test'))
    print(url_for('redirected'))







app.run(host='0.0.0.0', port=8080, debug=True)

