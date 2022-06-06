from django.shortcuts import render, redirect


def index(request):
    context = {

    }
    return render(request, 'index.html', context)
# Create your views here.

def aboutMe(request):
    return render(request, "about-me.html")

def projects(request):
    return render(request, 'projects.html')

def education(request):
    return render(request, "education.html")