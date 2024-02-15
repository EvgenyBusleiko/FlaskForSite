from pathlib import PurePath, Path
from flask import Flask, request, render_template

app = Flask(__name__)
# @app.route('/')
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')

        return f"Файл {file} загружен на сервер"
    return render_template('load.html')


if __name__ == '__main__':
    app.run(debug=True)
