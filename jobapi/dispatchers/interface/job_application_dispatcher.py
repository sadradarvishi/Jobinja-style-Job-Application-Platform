from django.urls import path

from jobapi.controllers.job_application_controller import JobApplicationController

urlpatterns = [
    path('', JobApplicationController.as_view())
]