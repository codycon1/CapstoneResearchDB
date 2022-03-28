from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView
from .forms import UploadFileForm
from .models import *
from proposal.models import proposal
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, 'home.html')


def SearchRequest(request):
    if request.method == 'GET':
        projectName = request.GET.get("search")
        status = Project.objects.filter(
            Q(projectTitle__icontains=projectName) | Q(projectAuthor__icontains=projectName))
        return render(request, "SearchResults.html", {"projects": status})
    else:
        return render(request, "SearchResults.html", {})


def saveFileUpload(request):
    form = UploadFileForm()
    try:
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                project_info = form.instance()
                return render(request, 'fileupload.html', {'form': form, 'project_info': project_info})
            else:
                form = UploadFileForm()
            return render(request, 'fileupload.html', {'form': form})
    except Exception as identifier:
        print(identifier)
    return render(request, 'fileupload.html', {'form': form})


@login_required
def approveProposal(request):
    context = {}
    context['pending'] = proposal.objects.filter(approval=False)

    if request.method == 'POST':
        id = request.POST.get('id', 0)
        proposalObject = proposal.objects.get(id=request.POST['id'])
        title = request.POST.get('title', "")
        if 'approve' in request.POST:
            proposalObject.approval = True
            proposalObject.save()
        elif 'delete' in request.POST:
            proposalObject.delete()
    else:
        pass
    return render(request, 'approveproposal.html', context)
