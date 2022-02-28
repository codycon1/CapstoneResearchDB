from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import *
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def saveFileUpload(request):
    saved = False
    if request.method == 'POST':
        capturedForm = UploadFileForm(request.POST, request.FILES)
        if capturedForm.is_valid():
            file = request.FILES['file']
            fs = FileSystemStorage()
            form = UploadFileForm()
            form.projectAuthor = capturedForm.cleaned_data['projectAuthor']
            form.projectTitle = capturedForm.cleaned_data['projectTitle']
            form.date = capturedForm.cleaned_data['date']
            filename = fs.save(file.name, file)
            file_url = fs.url(filename)
            saved = True
    else:
        capturedForm = UploadFileForm()
    return render(request, 'saved.html', locals())
