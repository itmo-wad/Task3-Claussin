from flask import Flask, render_template, send_from_directory, request, redirect


app = Flask(__name__)

app.secret_key = 'key'

db = {'pseudo': 'qwertyuiop'}

logged = False

@app.route('/', methods=['GET', 'POST'])
def login():
    try:
        if db[request.form['user']] == request.form['password']:
            logged = True
            return redirect('cabinet')
    except:
        msg = "Request error"
    return render_template('login.html')

@app.route('/cabinet')
def cabinet():
    if logged == True:
        return render_template('index.html')
    else:
        return render_template('login.html')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/img/<path:path>')
def index2(path):
    return send_from_directory('static/images', path)


@app.route('/static/<path:path>')
def index3(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run(threaded=True, port='5000')
