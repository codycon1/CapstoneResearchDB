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
    return render(request, 'home.html', context)


def viewSubmissions(request):
    userInfo = initialize_context(request)
    context = {'accepted': Project.objects.filter(approval=True, projectAuthor=userInfo['user']['name']),
               'pending': Project.objects.filter(approval=False, projectAuthor=userInfo['user']['name']),
               'user': userInfo['user']}
    return render(request, 'myproposals.html', context)


def SearchRequest(request):
    context = initialize_context(request)
    user = context['user']
    if request.method == 'GET':
        projectName = request.GET.get("search")
        status = Project.objects.filter(
            Q(projectTitle__icontains=projectName, approval=True) | Q(projectAuthor__icontains=projectName,
                                                                      approval=True))
        return render(request, "SearchResults.html", {"projects": status, 'user': user})
    else:
        return render(request, "SearchResults.html", {'user': user})


def saveFileUpload(request):
    context = initialize_context(request)
    authorName = context['user']['name']
    form = UploadFileForm(initial={'projectAuthor': authorName})
    try:
        if request.method == 'POST':
            print(authorName)
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                project_info = form.instance()
                return render(request, 'fileupload.html',
                              {'form': form, 'project_info': project_info, 'user': context['user']})
            else:
                form = UploadFileForm()
            return render(request, 'fileupload.html', {'form': form, 'user': context['user']})
    except Exception as identifier:
        print(identifier)
    return render(request, 'fileupload.html', {'form': form, 'user': context['user']})


def approveProposal(request):
    userInfo = initialize_context(request)
    context = {'pending': Project.objects.filter(approval=False), 'user': userInfo['user']}
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
