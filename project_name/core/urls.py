from django.conf.urls import include, patterns, url


urlpatterns = patterns("{{ project_name }}.core.views",
    url(r"^$", "hello_world", name="hello-world"),
)
