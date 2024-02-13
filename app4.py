from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    names =[
        {'name':'IVAN',
        'Lastname':'IVANOV',
         'age': 48},
        {'name': 'IVAN',
         'Lastname': 'IVANOV',
        'age': 48},
    ]
    return render_template ('table.html',context=names)




if __name__ == '__main__':
    app.run(debug=True)