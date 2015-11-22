import datetime
from ..models import Video

class VideoUtility:
	def get_video(self, video_id):
		video_detail = Video.query(Video.video_id == video_id)

		if video_detail == None:
			today = datetime.datetime.today()
			video_detail = Video.query(Video.upload_date <= today)

		return video_detail

	def get_related_video(self, video_id):
		return