from django.db import models
from google.appengine.ext import ndb

# Create your models here.
class Video(ndb.Model):
	video_id = ndb.StringProperty()
	upload_date = ndb.DateProperty()
	title = ndb.StringProperty()
	description = ndb.TextProperty()
	thumbnail = ndb.StringProperty()
	solar_term = ndb.StringProperty()
