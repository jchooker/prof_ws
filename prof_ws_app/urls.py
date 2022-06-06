from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('aboutMe', views.aboutMe),
    path('projects', views.projects),
    path('education', views.education)
]