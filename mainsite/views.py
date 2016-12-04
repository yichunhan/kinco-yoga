from django.shortcuts import render_to_response
from mainsite.modules.cronjob import CronJob
from mainsite.modules.video_utility import VideoUtility

def home(request):
	passed_dict = {}
	return render_to_response('home.html', passed_dict)

def purpose(request):
	passed_dict = {}
	return render_to_response('purpose.html', passed_dict)

def introduction(request):
	passed_dict = {}
	return render_to_response('introduction.html', passed_dict)

def coaches(request, teacher_name=None):
	passed_dict = {}
	return render_to_response('coaches.html', passed_dict)

def classes(request, class_index=None):
	passed_dict = {}
	return render_to_response('classes.html', passed_dict)

def videos(request):
	passed_dict = {}
	return render_to_response('videos.html', passed_dict)

def experiences(request, role=None):
	passed_dict = {}
	return render_to_response('experiences.html', passed_dict)

def articles(request, article_type=None):
	passed_dict = {}
	return render_to_response('articles.html', passed_dict)

def q_and_a(request):
	passed_dict = {}
	return render_to_response('q_and_a.html', passed_dict)

def cron_check_video(request):
	cronjob = CronJob()
	status = cronjob.check_videos()

	return render_to_response('dummy_cronjob_page.html')
