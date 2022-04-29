from django.urls import re_path as url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path

from capstone import settings
from home import views
from home.views import SearchRequest

"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
urlpatterns = [
                  path('', views.home, name='home'),
                  path('Search/', views.SearchRequest, name='Search'),
                  path('submit/', views.saveFileUpload, name='saveFileUpload'),
                  path('saved/', views.saveFileUpload, name="saved"),
                  path('SearchResults/', SearchRequest, name="SearchRequest"),
                  path('submissions/', views.viewSubmissions, name="submissions"),
                  path('changeApproval/', views.approveProposal, name="changeApproval"),
                  path('Unauthorized/', views.unauthorized, name="unauthorized"),
                  path('projectdetail/', views.ProjectDetail, name="projectDetail"),
                  path('generalFiles/', views.getGeneralFiles, name='generalFiles'),
                  path('dataFiles/', views.getDataSetFiles, name="dataFiles"),
                  path('resultFiles/', views.getResultFiles, name='resultFiles')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
