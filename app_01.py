from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        session['name'] = name
        session['email'] = email
        return redirect('/welcome')
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    if 'name' in session:
        return render_template('app_01.html', name=session['name'])
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('name', None)
    session.pop('email', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)