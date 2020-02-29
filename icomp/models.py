from icomp import db

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	email = db.Column(db.String(120),unique=True,nullable=False)
	password = db.Column(db.String(60),nullable=False)

	def __repr__(self):
		return f"User('{self.username}','{self.email}')"

class News(db.Model):
	n_id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(20),unique=True,nullable=False)
	content = db.Column(db.String(100),nullable=False)

	def __repr__(self):
		return f"News('{self.title}','{self.content}')"