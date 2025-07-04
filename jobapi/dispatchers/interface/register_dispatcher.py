from django.urls import path

from jobapi.controllers.register_controller import RegisterController

urlpatterns=[
    path('', RegisterController.as_view())
]