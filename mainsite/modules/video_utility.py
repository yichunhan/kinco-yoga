import datetime
from ..models import Video

class VideoUtility:
	def get_video(self, video_id=None):

		if video_id == None:
			today = datetime.datetime.today()
			video_detail = Video.query(Video.upload_date <= today).order(-Video.upload_date).get()
		else:
			video_detail = Video.query(Video.video_id == video_id).get()

		return video_detail

	def get_related_video(self, video_detail):
		related_video_details = Video.query(Video.solar_term == video_detail.solar_term).fetch(4)
		return related_video_details