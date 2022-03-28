from django.urls import path

from proposal import views

urlpatterns = [
    path('/submitproposal', views.submit_proposal)
]