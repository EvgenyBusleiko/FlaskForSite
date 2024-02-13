from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Введите путь к файлу в адресной строке'

@app.route('/<path:file>/')
def set_path(file):
    return f'Путь до файла {file}'

if __name__ == '__main__':
    app.run(debug=True)
