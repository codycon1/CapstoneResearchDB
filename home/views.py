import datetime
from itertools import chain
import zipfile

from django.core.exceptions import ValidationError
from django.http import FileResponse, HttpResponse, HttpResponseNotFound
from pytz import timezone
from django.db.models import Q
from django.shortcuts import render, redirect
from zipfile import *
from users.views import initialize_context
from .forms import *
from .models import *


# Create your views here.
def home(request):
    context = initialize_context(request)
    return render(request, 'home.html', context)


def getGeneralFiles(request):
    title = request.GET.get('title')
    dataFiles = ProjectFile.objects.filter(
        projectID__in=Project.objects.filter(projectTitle=title)).values('file')
    fileName = 'projects/projects/datasets/' + title + '.zip'
    zipFileObj = zipfile.ZipFile(fileName, 'w')
    for file in dataFiles:
        for i in file:
            zipFileObj.write('projects/' + file[i])
    zipFileObj.close()
    zip_file = open(fileName, 'rb')
    return FileResponse(zip_file)


def getDataSetFiles(request):
    title = request.GET.get('title')
    dataFiles = ProjectFile.objects.filter(
        projectID__in=Project.objects.filter(projectTitle=title)).values('file')
    fileName = 'projects/projects/datasets/' + title + '.zip'
    zipFileObj = zipfile.ZipFile(fileName, 'w')
    for file in dataFiles:
        for i in file:
            zipFileObj.write('projects/' + file[i])
    zipFileObj.close()
    zip_file = open(fileName, 'rb')
    return FileResponse(zip_file)


def getResultFiles(request):
    title = request.GET.get('title')
    resultFiles = ProjectFile.objects.filter(
        projectID__in=Project.objects.filter(projectTitle=title)).values('file')
    fileName = 'projects/projects/results' + title + '.zip'
    zipFileObj = zipfile.ZipFile(fileName, 'w')
    for file in resultFiles:
        for i in file:
            zipFileObj.write('projects/' + file[i])
    zipFileObj.close()
    zip_file = open(fileName, 'rb')
    return FileResponse(zip_file)


def viewSubmissions(request):
    userInfo = request.session
    uploadForm = UploadProjectFile(request.POST, request.FILES)
    context = {'form': uploadForm, }
    if request.method == 'POST':
        # try:
        uploadForm = UploadProjectFile(request.POST, request.FILES)
        authorEmail = request.session['user']['email']

        if uploadForm.is_valid():
            formdata = uploadForm.save(commit=False)
            formdata.userEmail = authorEmail
            id = request.POST.get('id', None)
            formdata.projectID = Project.objects.get(id=id)
            formdata.type = request.POST.get('type', None)
            formdata.save()
    # except:
    #     return render(request, 'myproposals.html', context)

    return render(request, 'myproposals.html',
                  context={'accepted': Project.objects.filter(approval=True, email=userInfo['user']['email']),
                           'pending': Project.objects.filter(approval=False, email=userInfo['user']['email']),
                           'user': userInfo['user'], 'form': uploadForm})


def ProjectDetail(request):
    context = initialize_context(request)
    projectID = request.GET.get('id', default=None)
    if projectID is None:
        return redirect('/')
    project_instance = Project.objects.get(id=projectID)

    if project_instance.email != request.session['user']['email']:
        return redirect('/submissions')

    project_generalfiles = ProjectFile.objects.filter(projectID_id=projectID, type=0)
    project_datafiles = ProjectFile.objects.filter(projectID_id=projectID, type=1)
    project_resultfiles = ProjectFile.objects.filter(projectID_id=projectID, type=2)

    uploadForm = UploadProjectFile()


    context['user'] = request.session['user']
    context['project'] = project_instance
    context['general'] = project_generalfiles
    context['data'] = project_datafiles
    context['result'] = project_resultfiles

    return render(request, 'projectdetail.html', context)


def SearchRequest(request):
    context = initialize_context(request)
    user = context['user']
    projectName = request.GET.get("search")
    if projectName:
        projects = Project.objects.filter(
            Q(projectTitle__icontains=projectName, approval=True) | Q(projectAuthor__icontains=projectName,
                                                                      approval=True))
        return render(request, "SearchResults.html",
                      {"projects": projects, 'user': user})
    else:
        return render(request, "SearchResults.html", {'user': user})


def saveFileUpload(request):
    try:
        context = request.session
        authorName = context['user']['name']
        authorEmail = context['user']['email']
        form = UploadFileForm(
            initial={'projectAuthor': authorName, 'email': authorEmail})
        try:
            if request.method == 'POST':
                form = UploadFileForm(request.POST, request.FILES)
                if form.is_valid():
                    projdata = form.save()
                    projdata.email = request.session['user']['email']
                    projdata.projectAuthor = request.session['user']['name']
                    projdata.save()
                    project_info = form.instance()
                    return render(request, 'fileupload.html',
                                  {'form': form, 'project_info': project_info, 'user': context['user']})
                else:
                    raise ValidationError(form.errors)
            return render(request, 'fileupload.html', {'form': UploadFileForm, 'user': context['user']})
        except Exception as identifier:
            print(identifier)
        return render(request, 'fileupload.html', {'form': form, 'user': context['user']})
    except:
        return render(request, 'UnauthorizedPage.html')


def unauthorized(request):
    return render(request, 'UnauthorizedPage.html')


def approveProposal(request):
    if not request.session['user']['is_staff']:
        return redirect('unauthorized')
    else:
        userInfo = request.session
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
