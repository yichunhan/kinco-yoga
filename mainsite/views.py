from django.shortcuts import render_to_response, redirect
from mainsite.modules.cronjob import CronJob
from mainsite.modules.coach_utility import CoachUtility
from mainsite.modules.class_utility import ClassUtility
from mainsite.modules.video_utility import VideoUtility
from mainsite.modules.experience_utility import ExperienceUtility
from mainsite.modules.faq_utility import FAQUtility
from mainsite.modules.home_utility import HomeUtility

def home(request):
	passed_dict = {}
	home_utility = HomeUtility()
	news = home_utility.get_news()

	passed_dict['news'] = news
	return render_to_response('home.html', passed_dict)

def coaches(request, coach_name=None):
	passed_dict = {}
	coach_utility = CoachUtility()
	return render_to_response('coach_all.html', passed_dict)	

def classes(request, class_index=None):
	passed_dict = {}
	class_utility = ClassUtility()
	return render_to_response('class_all.html', passed_dict)

def videos(request, video_type=None):
	passed_dict = {}
	video_utility = VideoUtility()
	videos = video_utility.get_videos(video_type)

	passed_dict['videos'] = videos
	passed_dict['video_type'] = video_type
	return render_to_response('video.html', passed_dict)

def experiences(request, role=None):
	passed_dict = {}
	experience_utility = ExperienceUtility()
	experiences = experience_utility.get_experiences(role)

	passed_dict['experiences'] = experiences 
	passed_dict['role'] = role
	return render_to_response('experiences.html', passed_dict)

def faq(request):
	passed_dict = {}
	faq_utility = FAQUtility()
	course_faqs, register_faqs = faq_utility.get_faqs()

	passed_dict['course_faqs'] = course_faqs
	passed_dict['register_faqs'] = register_faqs
	return render_to_response('faq.html', passed_dict)

def cron_check_video(request):
	cronjob = CronJob()
	status = cronjob.check_videos()

	return render_to_response('dummy_cronjob_page.html')
