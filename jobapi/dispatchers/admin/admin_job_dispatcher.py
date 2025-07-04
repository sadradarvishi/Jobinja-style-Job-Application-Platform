from django.urls import path
from jobapi.controllers.admin_controller.admin_job_controller import AdminJobController

urlpatterns = [
    path('', AdminJobController.as_view())
]