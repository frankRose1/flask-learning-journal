from peewee import *

DATABASE = SqliteDatabase('journal.db')

class BaseModel(Model):
	class Meta:
		database = DATABASE

class JournalEntry(BaseModel):
	# title
	# date
	# time spent
	# what was learned
	# resources to remember
