from django.conf.urls import patterns, url

import djappengine.sessions.views as views

urlpatterns = patterns('',
    url(r'^clean-up/$', views.session_clean_up, name='session-clean-up'),
)
