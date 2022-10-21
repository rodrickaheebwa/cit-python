from flask import Blueprint, request, redirect, render_template
from fruits.models import Fruit

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@views.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : num1 + num2
    }
    return render_template('calc.html', context=context)

# query parameters
# /add?num1=2&num2=6
@views.route('/add')
def add_query():
    num1 = int(request.args['num1'])
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return f"{num1} + {num2} = {result}"

@views.route('/fruits', methods = ['GET', 'POST'])
def fruits():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        price = request.form['price']
        fruit = Fruit(name=name, color=color, price=price)
        fruit.save()
        return redirect('/fruits')
        

    fruits = Fruit.get_all()
    return render_template('fruits.html', fruits=fruits)

# @views.route('/fruits/<option>')
# def fruit(option):
#     if option in fruit_list:
#         return option
#     else:
#         try:
#             return fruit_list[int(option)-1]
#         except:
#             return 'Invalid option'
