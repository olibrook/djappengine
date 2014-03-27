from django.conf import settings
from django.conf.urls import include, patterns, url


urlpatterns = patterns('',
    (r'^appengine_sessions/', include('appengine_sessions.urls')),

    (r'', include('{{ project_name }}.core.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('django.views.generic.simple',
        url(r'^500/$', 'direct_to_template', {'template': '500.html'}),
        url(r'^404/$', 'direct_to_template', {'template': '404.html'}),
    )
