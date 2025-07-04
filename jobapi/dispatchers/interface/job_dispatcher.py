from django.urls import path, include
from jobapi.controllers.job_controller import JobController

urlpatterns = [
    path('', JobController.as_view())
]