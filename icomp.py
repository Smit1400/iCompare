from flask import Flask, render_template, url_for ,flash
from forms import SignUpForm,LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '96e582be6947f9b29b1cd0f615a33600'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	email = db.Column(db.String(120),unique=True,nullable=False)
	password = db.Column(db.String(60),nullable=False)

	def __repr__(self):
		return f"User('{self.username}','{self.email}')"

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/products")
def products():
	return render_template('products.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/signup",methods=['GET','POST'])
def signup():
	form = SignUpForm()
	if form.validate_on_submit():
		return redirect(url_for('home'))
        # flash(f'Account created for {form.username.data}!', 'success')
	return render_template('signup.html',form=form)

if '__name__' == '__main__':
	app.run(debug=True)