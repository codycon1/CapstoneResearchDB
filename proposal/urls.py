from django.urls import path

from proposal import views

urlpatterns = [
    path('submit', views.submit_proposal),
    path('mysubmissions', views.my_submissions)
]