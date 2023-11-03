from flask import Flask, url_for, request, send_file, redirect, abort, render_template


app = Flask(__name__, template_folder='D:\\pycharm\\pythonProject\\flask semester 3\\homeworks\\homework 1\\templates', static_folder='D:\\pycharm\\pythonProject\\flask semester 3\\homeworks\\homework 1\\static')

dishes = [
    {'dish': 'Піца Техас', 'price': 260},
    {'dish': 'Піца Барбекю', 'price': 234},
    {'dish': 'Піца Маргарита', 'price': 220}
]




@app.route('/')
def main_page():
    return render_template('index.html')




@app.route('/menu/')
def manu():
    context = {
        'title': 'menu',
        'dishes': dishes
    }
    return render_template('menu.html', **context)



@app.route('/new pizza/')
def new_pizza():
    return render_template('new_pizza.html')


app.run(host='0.0.0.0', port=8080, debug=True)