from appengine_sessions import views
from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    (r'', include('core.urls')),
    url(r'^cron/session-clean-up/$', views.SessionCleanUpCron.as_view(), {}, name='session-clean-up'),

)
