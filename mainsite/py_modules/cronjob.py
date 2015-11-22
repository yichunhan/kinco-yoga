import urllib2, datetime, re
from db_utility import DBUtility

class CronJob:
	feed_url = r'https://www.youtube.com/feeds/videos.xml?channel_id=UC6-xZA6zHroZRCvHxrA_2Og'

	def check_videos(self):
		db_utility = DBUtility()
		today = datetime.date.today().strftime('%Y-%m-%d')
		entry_ptn = re.compile('\<entry\>(.*?)\<\/entry\>', re.DOTALL)
		video_id_ptn = re.compile('\<yt\:videoId\>(.*?)\<\/yt\:videoId\>')		
		upload_date_ptn = re.compile('\<published\>(.*?)\<\/published\>')
		thumbnail_ptn = re.compile('\<media\:thumbnail url\=\"(.*?)\"')
		title_ptn = re.compile('\<media\:title\>(.*?)\<\/media\:title\>', re.DOTALL)
		description_ptn = re.compile('\<media\:description\>(.*?)\<\/media\:description\>', re.DOTALL)

		try:
			page = urllib2.urlopen(CronJob.feed_url)
		except urllib2.HTTPError:
			return False

		page_source = page.read()
		entries = entry_ptn.findall(page_source)

		for entry in entries:
			video_id = video_id_ptn.findall(entry)[0]
			title = title_ptn.findall(entry)[0]
			thumbnail = thumbnail_ptn.findall(entry)[0].replace('hqdefault.jpg', 'default.jpg')
			description = description_ptn.findall(entry)[0]
			upload_date = upload_date_ptn.findall(entry)[0].split('T')[0]

			if upload_date == today:
				upload_date = datetime.datetime.strptime(upload_date, '%Y-%m-%d')
				db_utility.store_video(title=title, description=description, solar_term='None',
									   video_id=video_id, upload_date=upload_date, thumbnail=thumbnail)

		return True

