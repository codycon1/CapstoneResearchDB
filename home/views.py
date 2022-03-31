from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView
from .forms import *
from .models import *
from proposal.models import proposal
from django.db.models import Q
from users.views import initialize_context
from microsoft_authentication.auth.auth_decorators import microsoft_login_required


# Create your views here.
def home(request):
    context = initialize_context(request)
    return render(request, 'home.html',context)


def viewSubmissions(request):
    context = initialize_context(request)
    user = context['user']
    context['accepted'] = Project.objects.filter(approval=True)
    context['pending'] = Project.objects.filter(approval=False)
    return render(request, 'myproposals.html', context)


def SearchRequest(request):
    if request.method == 'GET':
        projectName = request.GET.get("search")
        status = Project.objects.filter(
            Q(projectTitle__icontains=projectName) | Q(projectAuthor__icontains=projectName))
        return render(request, "SearchResults.html", {"projects": status})
    else:
        return render(request, "SearchResults.html", {})


def saveFileUpload(request):
    context = initialize_context(request)
    user = context['user']
    form = UploadFileForm()
    context['form'] = form
    try:
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                project_info = form.instance()
                context['form'] = form
                context['project_info'] = project_info
                return render(request, 'fileupload.html', context)
            else:
                form = UploadFileForm()
                context['form'] = form
            return render(request, 'fileupload.html', context)
    except Exception as identifier:
        print(identifier)
    return render(request, 'fileupload.html', context)


def approveProposal(request):
    context = initialize_context(request)
    user = context['user']
    context['pending'] = Project.objects.filter(approval=False)
    if request.method == 'POST':
        id = request.POST.get('id', 0)
        proposalObject = Project.objects.get(id=request.POST['id'])
        title = request.POST.get('projectTitle', "")
        if 'approve' in request.POST:
            proposalObject.approval = True
            proposalObject.save()
        elif 'delete' in request.POST:
            proposalObject.delete()
    else:
        pass
    return render(request, 'approveproposal.html', context)
