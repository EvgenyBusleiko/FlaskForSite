from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index1/')
def index():
    return render_template('index1.html')
@app.route('/man/')
def man():
    return render_template('man.html')
@app.route('/woman/')
def woman():
    return render_template('woman.html')
@app.route('/kid/')
def kid():
    return render_template('kid.html')







if __name__ == '__main__':
    app.run(debug=True)