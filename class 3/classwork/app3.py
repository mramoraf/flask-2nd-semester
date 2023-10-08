from flask import Flask, render_template
import random as r

app = Flask(__name__, template_folder='D:\\pycharm\\pythonProject\\flask semester 3\\class 3\\classwork\\templates')

# hero = ['Warior', 'Wizard', 'Mag', 'Archer', 'Orc']

max_score = 100
test_name = 'Python Challenge'
students = [
    {'name': 'Vlad', 'score': 92},
    {'name': 'Svyt', 'score': 56},
    {'name': 'Alex', 'score': 78},
    {'name': 'Rimma', 'score': 100},
    {'name': 'Oleh', 'score': 99},
    {'name': 'Yaroslav', 'score': 98},
    {'name': 'Timofei', 'score': 85}
]



items = [
    {'item': 'cabige', 'price': 20, 'description': 'white vegetable'},
    {'item': 'cucumber', 'price': 70, 'description': 'green vegetable'},
    {'item': 'apple', 'price': 49, 'description': 'yellow vegetable'},
    {'item': 'tomato', 'price': 60, 'description': 'red vegetable'},
    {'item': 'potato', 'price': 40, 'description': 'brown vegetable'}
]


@app.route('/')
def hello_world():
    return render_template('base.html', title='all works fine')



@app.route('/index/')
def index():
    return render_template('base.html', title="All work fine")


@app.route('/results/')
def results():
    context = {
        'title': 'Results',
        'students': students,
        'test_name': test_name,
        'max_score': max_score
    }
    return render_template('results.html', **context)

# content = {
#     'posts': posts
# }
# @app.route('/status/')
# def status():
#     return render_template('status.html', **content)


content = {
    'products': items
}
@app.route('/products/')
def items():
    return render_template('price.html', **content)






app.run(host='0.0.0.0', port=8080, debug=True)


