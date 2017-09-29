from django.shortcuts import render_to_response, redirect
from mainsite.modules.cronjob import CronJob
from mainsite.modules.coach_utility import CoachUtility
from mainsite.modules.class_utility import ClassUtility
from mainsite.modules.video_utility import VideoUtility

def home(request):
	passed_dict = {}
	return render_to_response('home.html', passed_dict)

def coaches(request, coach_name=None):
	passed_dict = {}
	coach_utility = CoachUtility()
	return render_to_response('coach_all.html', passed_dict)	

def classes(request, class_index=None):
	passed_dict = {}
	class_utility = ClassUtility()
	return render_to_response('class_all.html', passed_dict)

def videos(request):
	passed_dict = {}
	return render_to_response('video.html', passed_dict)

def experiences(request, role=None):
	passed_dict = {}
	return render_to_response('experiences.html', passed_dict)

def q_and_a(request):
	passed_dict = {}
	return render_to_response('q_and_a.html', passed_dict)

def cron_check_video(request):
	cronjob = CronJob()
	status = cronjob.check_videos()

	return render_to_response('dummy_cronjob_page.html')
