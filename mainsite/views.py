from django.shortcuts import render_to_response, redirect
from mainsite.modules.cronjob import CronJob
from mainsite.modules.coach_utility import CoachUtility
from mainsite.modules.class_utility import ClassUtility
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

def coaches(request, coach_name=None):
	passed_dict = {}
	coach_utility = CoachUtility()

	if coach_name:
		coach_info = coach_utility.get_coach_info(coach_name.lower())
		if coach_info:
			passed_dict['coach_info'] = coach_info
			return render_to_response('coach_one.html', passed_dict)
		return redirect('/coaches/')
	return render_to_response('coach_all.html', passed_dict)

def classes(request, class_index=None):
	passed_dict = {}
	class_utility = ClassUtility()

	if class_index:
		class_info = class_utility.get_class_info(class_index)
		if class_info:
			passed_dict['class_info'] = class_info
			return render_to_response('class_one.html', passed_dict)
		return redirect('/classes/')
	return render_to_response('class_all.html', passed_dict)

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
