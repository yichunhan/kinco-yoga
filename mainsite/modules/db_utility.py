from ..models import FAQ
from ..models import News
from ..models import Video
from ..models import Coach
from ..models import Class
from ..models import Experience

class DBUtility:
	def get_coach_info(self, coach_name):
		return Coach.query(Coach.name==coach_name).get()

	def get_class_info(self, class_index):
		return Class.query(Class.index==class_index).get()

	def get_experiences(self, role):
		return Experience.query(Experience.role == role)

	def store_video(self, **kwargs):
		store_document = Video(**kwargs)
		store_key = store_document.put()
		return store_key

	def search_video(self, operator, **kwargs):
		if operator == '==':
			return Video.query(*(getattr(Video, k)==v for (k,v) in kwargs.items())).get()
		elif operator == '<=':
			return Video.query(*(getattr(Video, k)<=v for (k,v) in kwargs.items())).order(-Video.upload_date).get()
	
	def get_videos(self, video_type):
		if video_type in ['class', 'tv']:
			# return Video.query(Video.video_type == video_type).order(-Video.upload_date).get()
			return Video.query(Video.video_type == video_type)
		else:
			return Video.query(Video.video_id == video_type).get()

	def get_faqs(self, faq_type):
		return FAQ.query(FAQ.faq_type == faq_type)

	def get_news(self):
		return News.query().order(-News.publish_date)