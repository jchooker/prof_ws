from django.shortcuts import render, redirect


def index(request):
    context = {

    }
    return render(request, 'index.html', context)
# Create your views here.

def aboutMe(request):
    return render(request, "about-me.html")
