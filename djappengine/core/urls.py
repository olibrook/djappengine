from django.conf.urls import include, patterns, url


urlpatterns = patterns("djappengine.core.views",
    url(r"^$", "hello_world", name="hello-world"),
)
