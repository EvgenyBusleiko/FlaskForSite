from flask import Flask, render_template, request

app = Flask(__name__)

app.route('/')
def inedex():
    return render_template('password.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('login')
        password = request.form.get('password')
        print(name,password)
        print(request.form)
        if name == 'admin' and password == 'password':
            return "Вы вошли"
        else:
            return "Мимо"

    return render_template('password.html')


if __name__ == '__main__':
    app.run(debug=True)
