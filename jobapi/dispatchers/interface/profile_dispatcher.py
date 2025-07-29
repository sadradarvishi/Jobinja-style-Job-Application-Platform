from django.urls import path
from jobapi.controllers.profile_controller import ProfileController

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProfileController.as_view())
 ]