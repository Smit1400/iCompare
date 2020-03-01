from flask import render_template,redirect ,url_for ,flash
from icomp.forms import SignUpForm,LoginForm
from icomp.models import User ,News
from icomp import app ,db ,bcrypt

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

@app.route("/login" ,methods=['POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		flash('You have been successfully logged in!' ,'success')
		return redirect(url_for('home'))
	return render_template('login.html',form=form)

@app.route("/signup",methods=['GET','POST'])
def signup():
	form = SignUpForm()
	if form.validate_on_submit():
		hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data,email=form.email.data,password=hashed_pass)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created successfully for  { form.username.data }' ,'success')
		return redirect(url_for('home'))
	return render_template('signup.html',form=form)