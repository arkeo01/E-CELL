from __future__ import absolute_import
from django.views.generic.base import TemplateView
from blogs.models import blog


class BlogHome(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHome, self).get_context_data(**kwargs)
        context['articles'] = blog.objects.all()
        return context
