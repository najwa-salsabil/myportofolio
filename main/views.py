from django.shortcuts import render

from main.models import Experience, Project, Achievement


def show_main(request):
    context = {
        "name": "Najwa Salsabil",
        "npm": "2506588701",
        "study_program": "S1 Information System",
        "bio": (
            "Information Systems student at Universitas Indonesia passionate about web development, technology exploration, and Business. Currently learning to build clean, functional, and scalable applications through modern web platforms. Always excited to tackle new challenges and collaborate on impactful projects."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Najwa Salsabil",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        "name": "Najwa Salsabil",
        "project_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)

def show_achievements(request):
    context = {
        "name": "Najwa Salsabil",
        "achievement_list": Achievement.objects.all(),
    }
    return render(request, "achievements.html", context)