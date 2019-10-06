from django.shortcuts import render
from projects.models import Project

# Create your views here.


def project_index(request):
    # query - create, retrieve, update, or delete objects in database
    projects = Project.objects.all()
    # define dictionary context - only has 1 entry projects, assigns Queryset containing all projects
    # context is used to send info to templates. every view func create needs to have a context dict.
    context = {
        "projects": projects
    }
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    # query - retrieve project with pk equal to that in func arg.
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
