from django.urls import path
from jobapi.controllers.profile_controller import ProfileController

urlpatterns = [
    path('', ProfileController.as_view())
]