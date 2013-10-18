from django.views.generic import TemplateView


class HelloWorld(TemplateView):
    template_name = "hello-world.html"

    def get_context_data(self, **kwargs):
        context = super(HelloWorld, self).get_context_data(**kwargs)
        self.request.session['test'] = 'Session is working'
        context['message'] = 'Hooray! Everything seems to work... - %s' % self.request.session['test']
        return context

hello_world = HelloWorld.as_view()
