from django.db import models


from jobapi.entity.job_entity import JobEntity
from jobapi.entity.user_entity import UserEntity


class JobApplicationEntity(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'job'], name='unique_job_application')
        ]

    user = models.ForeignKey(UserEntity, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(JobEntity, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
