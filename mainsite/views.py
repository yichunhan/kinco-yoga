from django.shortcuts import render_to_response
from mainsite.py_modules.cronjob import CronJob
from mainsite.py_modules.video_utility import VideoUtility

def home(request):
	passed_dict = {}
	return render_to_response('home.html', passed_dict) 

def video(request):
	passed_dict = {}
	video_utility = VideoUtility()

	video_id = request.GET.get('id')
	video_detail = video_utility.get_video(video_id)
	related_video_details = video_utility.get_related_video(video_id)
	passed_dict['video_detail'] = video_detail
	
	return render_to_response('video.html', passed_dict) 

def cron_check_video(request):
	cronjob = CronJob()
	status = cronjob.check_videos()

	return render_to_response('dummy_cronjob_page.html')