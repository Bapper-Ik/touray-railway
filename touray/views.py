from django.shortcuts import render
from .models import Posts, Audio


def home(request):
    return render(request, 'touray/home.html')


def resources(request):
    audious = Audio.objects.all()
    context = {"audious": audious}
    return render(request, 'touray/resources.html', context)


def newsFeed(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'touray/post.html', context)


def donation(request):
    return render(request, 'touray/donation.html')


def mosque(request):
    return render(request, 'touray/mosque.html')


def about(request):
    return render(request, 'touray/about.html')


def contact(request):
    return render(request, 'touray/contact.html')
