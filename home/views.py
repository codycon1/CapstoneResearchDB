import datetime
from itertools import chain
import zipfile
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


# def submit_proposal(request):
#     context = initialize_context(request)
#     user = request.session
#     if request.method == 'POST':
#         form = SubmitProposalForm(request.POST)
#         if form.is_valid():
#             p = form.save(commit=False)
#             p.author = user['user']['name']
#             p.email = user['user']['email']
#             p.save()
#             return redirect('/')
#     else:
#         form = SubmitProposalForm()
#
#     context['form'] = form
#     return render(request, 'newproposal.html', context)


def getDataSetFiles(request):
    title = request.GET.get('title')
    dataFiles = ProjectFile.objects.filter(
        projectID__in=Project.objects.filter(projectTitle=title)).values('dataFile')
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
    resultFiles = ResultFile.objects.filter(
        projectID__in=Project.objects.filter(projectTitle=title)).values('resultFile')
    fileName = 'projects/projects/results' + title + '.zip'
    zipFileObj = zipfile.ZipFile(fileName, 'w')
    for file in resultFiles:
        for i in file:
            zipFileObj.write('projects/' + file[i])
    zipFileObj.close()
    zip_file = open(fileName, 'rb')
    return FileResponse(zip_file)


def viewSubmissions(request):
    dataSets = []
    userInfo = request.session
    if request.method == 'POST':
        file = request.POST.get('file', None)
        filetype = request.POST.get('type', None)
        id = request.POST.get('id', None)
        file = request.FILES['file']
        id = int(id)
        filetype = int(filetype)
        projectTitle = request.POST.get('dataTitle')
        if file is not None and filetype == 1:
            for file in request.FILES.getlist('file'):
                obj, created = ProjectFile.objects.update_or_create(
                    projectID=Project(id=id, projectTitle=projectTitle, email=request.session['user']['email']),
                    dataFile=file, type=filetype, userEmail=userInfo['user']['email'])
                obj.save()
            return render(request, 'myproposals.html', context={
                'accepted': Project.objects.filter(approval=True, email=userInfo['user']['email']),
                'pending': Project.objects.filter(approval=False, email=userInfo['user']['email']),
                'user': userInfo['user']})
        if file is not None and filetype == 2:
            obj, created = ResultFile.objects.update_or_create(
                projectID=Project(id=id, projectTitle=projectTitle, email=request.session['user']['email']),
                resultFile=file, type=filetype, userEmail=request.session['user']['email'])
            obj.save()
            return render(request, 'myproposals.html',
                          context={'accepted': Project.objects.filter(approval=True, email=userInfo['user']['email']),
                                   'pending': Project.objects.filter(approval=False, email=userInfo['user']['email']),
                                   'user': userInfo['user']})
    return render(request, 'myproposals.html',
                  context={'accepted': Project.objects.filter(approval=True, email=userInfo['user']['email']),
                           'pending': Project.objects.filter(approval=False, email=userInfo['user']['email']),
                           'user': userInfo['user']})


def ProjectDetail(request):
    projectID = request.GET.get('id', default=None)
    print(projectID)
    if projectID is None:
        return redirect('/')
    project_instance = Project.objects.get(pk=id)
    print(project_instance.projectTitle)

    context = {}
    return render(request, 'projectdetail.html', context)


def SearchRequest(request):
    context = initialize_context(request)
    user = context['user']
    projectName = request.GET.get("search")
    if projectName:
        projects = Project.objects.filter(
            Q(projectTitle__icontains=projectName, approval=True) | Q(projectAuthor__icontains=projectName,
                                                                      approval=True))
        datasets = ProjectFile.objects.filter(
            Q(projectID__in=Project.objects.filter(projectTitle__icontains=projectName, approval=True)) | Q(
                projectID__in=Project.objects.filter(projectAuthor__icontains=projectName,
                                                     approval=True)))
        results = ResultFile.objects.filter(
            Q(projectID__in=Project.objects.filter(projectTitle__icontains=projectName, approval=True)) | Q(
                projectID__in=Project.objects.filter(projectAuthor__icontains=projectName,
                                                     approval=True)))
        status = chain(projects, datasets, results)
        return render(request, "SearchResults.html",
                      {"projects": status, 'user': user})
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
                    form = UploadFileForm()
                return render(request, 'fileupload.html', {'form': form, 'user': context['user']})
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


def projectDetail(request):
    return None
