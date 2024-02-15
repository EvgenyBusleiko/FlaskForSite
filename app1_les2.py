from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('name.html')








if __name__ == '__main__':
    app.run(debug=True)