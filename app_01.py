from flask import Flask

app = Flask(__name__)


@app.route('/<line>/')
def hello_world(line):
    sum=len(line)
    return f'Длина строки {line} = {sum}'
@app.route('/about/')
def nike():
    return 'About'


@app.route('/contact/')
def ian():
    return 'Контакты'

if __name__ == '__main__':
    app.run()
