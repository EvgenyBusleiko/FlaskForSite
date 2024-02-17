from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/submit', methods=['GET', 'POST'])
def submit():

    if request.method == 'POST':
        name = request.form.get('login')
        password = request.form.get('email')

        # print(request.cookies.get('login'))
        # print(request.cookies.get('pas'))


        response = make_response(render_template('welcome.html', contex=name))
        response.set_cookie('login', value=name)
        response.set_cookie('pas', value=password)
        return response

    return render_template('password.html')




@app.route('/', methods=['GET', 'POST'])
def redirect_to_inedex():
    return redirect(url_for('submit'))


@app.route('/forward/', methods=['GET', 'POST'])
def return_to_main():
    if request.method == 'POST':
        response = make_response(render_template('password.html'))
        response.set_cookie('login', max_age=0)
        response.set_cookie('pas', max_age=0)
        return response
    return render_template('password.html')


if __name__ == '__main__':
    app.run(debug=True)
