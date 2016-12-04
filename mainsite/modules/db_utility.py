from ..models import Video

class DBUtility:
	def store_video(self, **kwargs):
		store_document = Video(**kwargs)
		store_key = store_document.put()
		return store_key

	def search_video(self, operator, **kwargs):
		if operator == '==':
			return Video.query(*(getattr(Video, k)==v for (k,v) in kwargs.items())).get()
		elif operator == '<=':
			return Video.query(*(getattr(Video, k)<=v for (k,v) in kwargs.items())).order(-Video.upload_date).get()