from db_utility import DBUtility

class VideoUtility:
	def get_videos(self, video_type):	
		db_utility = DBUtility()
		video_details = db_utility.get_videos(video_type)

		return video_details

	def get_related_video(self, video_detail):
		related_video_details = Video.query(Video.solar_term == video_detail.solar_term).fetch(4)
		return related_video_details