import datetime
from db_utility import DBUtility

class VideoUtility:
	def get_video(self, video_id):
		db_utility = DBUtility()
		video_detail = db_utility.search_video('==', video_id=video_id)

		if video_detail == None:
			today = datetime.datetime.today()
			video_detail = db_utility.search_video('<=', upload_date=today)

		return video_detail

	def get_related_video(self, video_id):
		return