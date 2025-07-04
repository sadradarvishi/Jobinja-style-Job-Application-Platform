from django.urls import path, include

urlpatterns = [
    path('jobs', include('jobapi.dispatchers.interface.job_dispatcher')),
    path('register', include('jobapi.dispatchers.interface.register_dispatcher')),
    path('profile', include('jobapi.dispatchers.interface.profile_dispatcher')),
    path('sign_up', include('jobapi.dispatchers.interface.sign_up_dispatcher')),
    path('job/apply', include('jobapi.dispatchers.interface.job_application_dispatcher'))
]