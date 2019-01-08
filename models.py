import datetime

from peewee import *
from flask_bcrypt import generate_password_hash
from flask_login import UserMixin

DATABASE = SqliteDatabase('journal.db')


class BaseModel(Model):
	class Meta:
		database = DATABASE


class User(UserMixin, BaseModel):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField()
	join_date = DateTimeField(default=datetime.datetime.now)

	@classmethod
	def create_user(cls, username, email, password):
		try:
			cls.create(
				username=username,
				email=email,
				password=generate_password_hash(password)
			)
		# except any errors from validation
		except IntegrityError:
			raise ValueError('Error registering user.')


class JournalEntry(BaseModel):
	title = CharField()
	date = DateTimeField(datetime.datetime.now)
	time_spent = CharField()
	what_i_learned = TextField()
	resources_to_remember = TextField()
	user = ForeignKeyField(
		rel_model=User,
		related_name='entries'
	)


def initialize():
	"""Ensures tables are created when app is started"""
	DATABASE.connect()
	DATABASE.create_tables([User, JournalEntry], safe=True)
	DATABASE.close()
