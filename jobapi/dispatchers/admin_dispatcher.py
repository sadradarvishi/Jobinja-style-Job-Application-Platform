from django.urls import path, include

urlpatterns = [
    path('job', include('jobapi.dispatchers.admin.admin_job_dispatcher')),
]