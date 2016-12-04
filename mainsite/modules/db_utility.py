from ..models import Video
from ..models import Coach
from ..models import Class

class DBUtility:
	def get_coach_info(self, coach_name):
		return Coach.query(Coach.name==coach_name).get()

	def get_class_info(self, class_index):
		return Class.query(Class.index==class_index).get()

	def store_video(self, **kwargs):
		store_document = Video(**kwargs)
		store_key = store_document.put()
		return store_key

	def search_video(self, operator, **kwargs):
		if operator == '==':
			return Video.query(*(getattr(Video, k)==v for (k,v) in kwargs.items())).get()
		elif operator == '<=':
			return Video.query(*(getattr(Video, k)<=v for (k,v) in kwargs.items())).order(-Video.upload_date).get()
