from django.shortcuts import render


def bloghome(request):
    return render(request,'blog.html')
