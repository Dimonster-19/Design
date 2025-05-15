from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    featured_projects = Project.objects.filter(is_featured=True)
    return render(request, 'main/index.html', {'projects': featured_projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'main/project_detail.html', {'project': project})