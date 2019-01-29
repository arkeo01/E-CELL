from django.views.generic import TemplateView


class BlogHome(TemplateView):
    template_name = 'blog.html'
