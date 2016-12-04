from django.db import models
from google.appengine.ext import ndb

# Create your models here.
class Coach(ndb.Model):
	name = ndb.StringProperty()
	display_name = ndb.StringProperty()
	experience = ndb.StringProperty()

class Class(ndb.Model):
	index = ndb.StringProperty() 
	name = ndb.StringProperty()
	coach = ndb.StringProperty()
	time = ndb.TimeProperty()
	weekday = ndb.StringProperty()
	introduction = ndb.StringProperty()
	benefit = ndb.StringProperty()
	target_audience = ndb.StringProperty()

class TV_Video(ndb.Model):
	title = ndb.StringProperty()
	source = ndb.StringProperty()
	introduction = ndb.StringProperty()
	url = ndb.StringProperty()

class ClassVideo(ndb.Model):
	title = ndb.StringProperty()
	solar_term = ndb.StringProperty()
	related_classes = ndb.StringProperty()
	introduction = ndb.StringProperty()
	url = ndb.StringProperty()

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
	publish_date = ndb.DateProperty()
	join_class = ndb.StringProperty()

class KincoArticle(ndb.Model):
	title = ndb.StringProperty()
	content = ndb.TextProperty()
	publish_date = ndb.DateProperty()

class OtherArticle(ndb.Model):
	author = ndb.StringProperty()
	title = ndb.StringProperty()
	content = ndb.TextProperty()
	publish_date = ndb.DateProperty()
	url = ndb.StringProperty()

class FAQ(ndb.Model):
	question = ndb.StringProperty()
	answer = ndb.TextProperty()

class Video(ndb.Model):
	video_id = ndb.StringProperty()
	upload_date = ndb.DateProperty()
	title = ndb.StringProperty()
	description = ndb.TextProperty()
	thumbnail = ndb.StringProperty()
	solar_term = ndb.StringProperty()
