from django.shortcuts import render
from resume.models import education, skill, project

# Create your views here.
def index(request):
    return render(request, 'home.html')

def education_view(request):
    resume = education.objects.all()
    context = {'resume': resume }
    return render(request, 'education_view.html', context)

def skill_view(request):
    resume = skill.objects.all()
    context = {'resume':resume}
    return render(request, 'skill_view.html', context)

def project_view(request):
    resume = project.objects.all()
    context ={'resume':resume}
    return render(request, 'project.html', context)