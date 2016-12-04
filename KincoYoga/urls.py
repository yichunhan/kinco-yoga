"""KincoYoga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^purpose/$', 'mainsite.views.purpose'),
    url(r'^introduction/$', 'mainsite.views.introduction'),
    url(r'^coaches/$', 'mainsite.views.coaches'),
    url(r'^classes/$', 'mainsite.views.classes'),
    url(r'^videos/$', 'mainsite.views.videos'),
    url(r'^experiences/$', 'mainsite.views.experiences'),
    url(r'^articles/$', 'mainsite.views.articles'),
    url(r'^q_and_a/$', 'mainsite.views.q_and_a'),
    url(r'^cron_check_video/$', 'mainsite.views.cron_check_video'),
    url(r'^$', 'mainsite.views.home'),
]
