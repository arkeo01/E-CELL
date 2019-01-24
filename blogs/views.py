from django.shortcuts import render
from .models import blog

def bloghome(request):
    articles = blog.objects.all().order_by('date')
    return render(request,'blog.html',{'articles':articles})
