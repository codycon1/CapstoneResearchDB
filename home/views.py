from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView
from .forms import *
from .models import *
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, 'home.html')


def SearchResults(ListView):
    model = Project
    template = 'SearchResults.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Project.objects.filter(
            Q(projectTitle__icontains=query) | Q(projectAuthor__icontains=query)
        )
        return object_list


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
