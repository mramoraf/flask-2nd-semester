from flask import Flask, url_for, request, send_file, redirect, abort, render_template

app = Flask(__name__, template_folder='D:\\pycharm\\pythonProject\\flask semester 3\\templates', static_folder='D:\\pycharm\\pythonProject\\flask semester 3\\static')
@app.route('/')
def index():
    return render_template('index.html')






app.run(host='0.0.0.0', port=8080, debug=True)
