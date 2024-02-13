from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def index(name='незнакомец'):
    return f'Привет, {name.capitalize()}!'


@app.route('/file/<path:file>/')
def set_path(file):
    return f'Путь до файла {file}'


@app.route('/number/<float:num>')
def ian(num):
    return f'Число {num}'

if __name__ == '__main__':
    app.run(debug=True)

