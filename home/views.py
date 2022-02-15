from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def saveFileUpload(request):
    saved = False
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form = UploadFileForm()
            form.projectAuthor = form.cleaned_data['projectAuthor']
            form.projectTitle = form.cleaned_data['projectTitle']
            form.date = form.cleaned_data['date']
            form.file = form.cleaned_data['file']
            form.save()
            saved = True
    else:
        form = UploadFileForm()
    return render(request, 'saved.html', locals())
