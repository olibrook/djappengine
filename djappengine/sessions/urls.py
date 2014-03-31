from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^clean-up/$', 'views.session_clean_up', name='session-clean-up'),
)
