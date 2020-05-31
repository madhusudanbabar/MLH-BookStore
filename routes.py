from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html');
