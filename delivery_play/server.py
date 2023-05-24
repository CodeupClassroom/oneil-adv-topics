from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello class!'

@app.route('/hello')
def greet_class():
    return render_template('first_template.html')

# lets create our first form
# forms require a special html element
# and require us to interact with the html in a new way

# we will need two functions (at least)
# an initial call that serves the content
# and a second one that renders the results
@app.route('/my_first_form')
def form():
    return render_template('form1.html')


@app.route('/process_form', methods=['POST'])
def process():
    title = request.form['title']
    name = request.form['name']
    greeting = f'Hello {title} {name}'
    return render_template('my_greeting.html', greeting=greeting)
    