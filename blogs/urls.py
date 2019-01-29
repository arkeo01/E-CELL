from django.conf.urls import url
from .views import BlogHome

urlpatterns = [
    url(r'^$', BlogHome.as_view()),
]
