# coding: utf-8
from django.conf.urls import include, url
#~ from .views import IssuesListView
#~ from .views import IssueDetailView
from .views import *
from django.conf import settings

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import login, logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
        url(r'^$', IssuesListView.as_view(), name='index'),
        url(r'^(?P<pk>[0-9]+)/$', IssueDetailView.as_view(), name='detail'),
        url(r'^register/$', RegisterView.as_view(), name='register'),
        url(r'^logout/$', logout, {'next_page': reverse_lazy('login')}, name="logout"),
        #~ url(r'^logout/$', logout(next_page=reverse_lazy('login')), name="logout"),
        url(r'^login/$', login, {'template_name': "login.html"}, name="login"),
        url(r'^add/$', IssueCreateView.as_view(), name='add'),
]

    
    
# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = staticfiles_urlpatterns() + urlpatterns
