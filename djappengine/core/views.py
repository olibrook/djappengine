from django.views.generic import TemplateView

hello_world = TemplateView.as_view(template_name='core/hello-world.html')
