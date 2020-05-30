from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = '47cb68fb89b29cc726f0cee40ae569a3'

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)