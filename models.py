import datetime

from peewee import *

DATABASE = SqliteDatabase('journal.db')


class BaseModel(Model):
	class Meta:
		database = DATABASE


class JournalEntry(BaseModel):
	title = CharField()
	date = DateTimeField(datetime.datetime.now)
	time_spent = CharField()
	what_i_learned = TextField()
	resources_to_remember = TextField()


class User(BaseModel):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField(max_length=100)
	join_date = DateTimeField(default=datetime.datetime.now)

	@classmethod
	def create_user(cls, username, email, password):
		try:
			cls.create(
				username=username,
				email=email,
				password=password
			)
		# except any errors from validation
		except IntegrityError:
			raise ValueError('User already exists')


def initialize():
	"""Ensures tables are created when app is started"""
	DATABASE.connect()
	DATABASE.create_tables([JournalEntry, User], safe=True)
	DATABASE.close()
