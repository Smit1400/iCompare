from flask import render_template,redirect ,url_for ,flash
from icomp.forms import SignUpForm,LoginForm
from icomp.models import User ,News
from icomp import app

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
		flash(f'Account created successfully for  { form.username.data }' ,'success')
		return redirect(url_for('home'))
	return render_template('signup.html',form=form)
