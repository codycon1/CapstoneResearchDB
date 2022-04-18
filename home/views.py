import datetime

from pytz import timezone
from django.db.models import Q
from django.shortcuts import render, redirect

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


def viewSubmissions(request):
    userInfo = request.session
    context = {'accepted': Project.objects.filter(approval=True, email=userInfo['user']['email']),
               'pending': Project.objects.filter(approval=False, email=userInfo['user']['email']),
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
                    projdata = form.save(commit=False)
                    projdata.email = request.session['user']['email']
                    projdata.projectAuthor = request.session['user']['name']
                    projdata.save()
                    project_info = form.instance()
                    return render(request, 'fileupload.html',
                                  {'form': form, 'project_info': project_info, 'user': context['user']})
                else:
                    print(form.errors)
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
    try:
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
    except:
        return redirect('unauthorized')
