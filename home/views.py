from django.shortcuts import render
from .forms import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def fileUpload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render('The file is saved')
        else:
            form = UploadFileForm()
            context = {
                'form': form,
            }
        return render(request, 'home.html', context)

