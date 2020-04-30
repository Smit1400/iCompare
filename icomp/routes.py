from flask import render_template,redirect ,url_for ,flash, request
from icomp.forms import SignUpForm,LoginForm
from icomp.models import User ,News
from icomp import app ,db ,bcrypt
from flask_login import login_user ,current_user ,logout_user
import pickle

my_model = pickle.load(open('model_pickel_final','rb'))


@app.route("/")
@app.route("/home",methods=['GET','POST'])
def home():
	news1 = News.query.first()
	news2 = News.query.filter_by(n_id=2).first()
	news3 = News.query.filter_by(n_id=3).first()
	return render_template('home.html',news1=news1,news2=news2,news3=news3)

@app.route("/about")
def about():
	return render_template('about_final.html')

@app.route("/products")
def products():
	return render_template('products_final.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
	if request.method == "POST":
		value = request.form["prediction"]
		print(value)
		return render_template('products_final.html',pred = value)
	# features = request.form.values()
	# print(features)

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route("/login" ,methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		redirect(url_for('home'))
	form=LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user,remember=form.remember.data)
			flash('You are successfully logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Check your email and password!')
	return render_template('login.html',form=form)


@app.route("/signup",methods=['GET','POST'])
def signup():
	if current_user.is_authenticated:
		redirect(url_for('home'))
	form = SignUpForm()
	if form.validate_on_submit():
		hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data,email=form.email.data,password=hashed_pass)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created successfully for  { form.username.data }' ,'success')
		return redirect(url_for('login'))
	return render_template('signup.html',form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))