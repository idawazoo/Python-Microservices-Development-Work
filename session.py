from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'philrocks'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
            "<b><a href = '/logout'>click here to log out</a></b>"

    return "You are not logged in <br><a href = '/login'></b>" + \
        "click here to log in</b></a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('login post1 request:{}'.format(request.form))
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return '''

    <form action = "/login" method = "POST">
        <p><input type = text name = username /></p>
        <p><input type = submit name = Login /></p>
    </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
