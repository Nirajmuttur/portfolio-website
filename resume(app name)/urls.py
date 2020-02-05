from django.urls import path
from . import views

urlpatterns = [
    path('', views.education_view, name='education_view'),
    path('home/', views.index, name='home'),
    path('skill/', views.skill_view, name='skill_view'),
    path('project/', views.project_view, name='project_view'),
]