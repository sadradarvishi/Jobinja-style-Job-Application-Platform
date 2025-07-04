from django.core.files.uploadedfile import UploadedFile

from jobapi.entity.job_application_entity import JobApplicationEntity

from typing import Optional

class JobApplicationDao:

    def create_application(
            self,
            job,
            user,
            resume: Optional[UploadedFile],
            note: Optional[str]
    ):
        return JobApplicationEntity.objects.create(
            job=job,
            user=user,
            resume=resume,
            note=note
        )

    def check_user_application(self, user, job):
        return JobApplicationEntity.objects.filter(user=user, job=job)

    def get_all_job_applications(self, user):
        return JobApplicationEntity.objects.filter(user=user)