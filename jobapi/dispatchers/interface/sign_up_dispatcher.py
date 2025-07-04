from django.urls import path, include

from jobapi.controllers.sign_up_controller import SignUpController

urlpatterns = [
    path('', SignUpController.as_view())
]