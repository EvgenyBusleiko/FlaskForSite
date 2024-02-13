from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello,world!'


@app.route('/about/')
def nike():
    return 'Привет, Николай!'


@app.route('/contacts/')
def ian():
    return 'Привет, Ванюша!'

if __name__ == '__main__':
    app.run(debug=True)

