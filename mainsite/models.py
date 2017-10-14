from django.db import models
from google.appengine.ext import ndb

class Coach(ndb.Model):
	name = ndb.StringProperty()
	display_name = ndb.StringProperty()
	experience = ndb.StringProperty()

class News(ndb.Model):
	publish_date = ndb.DateProperty()
	title = ndb.StringProperty()
	content = ndb.TextProperty()

class Class(ndb.Model):
	index = ndb.StringProperty() 
	name = ndb.StringProperty()
	coach = ndb.StringProperty()
	time = ndb.TimeProperty()
	weekday = ndb.StringProperty()
	introduction = ndb.StringProperty()
	benefit = ndb.StringProperty()
	target_audience = ndb.StringProperty()

class SolarTerm(ndb.Model):
	name = ndb.StringProperty()
	introduction = ndb.StringProperty()
	start_date = ndb.DateProperty()
	end_date = ndb.DateProperty()

class Experience(ndb.Model):
	author = ndb.StringProperty()
	age = ndb.IntegerProperty()
	photo_url = ndb.StringProperty()
	content = ndb.StringProperty()
	title = ndb.StringProperty()
	publish_date = ndb.DateProperty()
	join_class = ndb.StringProperty()
	male = ndb.BooleanProperty()
	role = ndb.StringProperty()

class FAQ(ndb.Model):
	question = ndb.StringProperty()
	answer = ndb.TextProperty()
	faq_type = ndb.StringProperty()

class Video(ndb.Model):
	video_id = ndb.StringProperty()
	upload_date = ndb.DateProperty()
	title = ndb.StringProperty()
	description = ndb.TextProperty()
	thumbnail = ndb.StringProperty()
	solar_term = ndb.StringProperty()
	video_type = ndb.StringProperty()
	video_source = ndb.StringProperty()
