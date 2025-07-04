from django.db import models

class JobEntity(models.Model):
    company_name = models.CharField(max_length=225, null=False)
    title = models.CharField(max_length=225, null=False)
    location = models.CharField(max_length=225, null=False)
    agreement = models.CharField(max_length=50, null=False, choices=[
        ('full_time', 'full_time'), ('part_time', 'part_time'), ('remote', 'remote')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    salary = models.IntegerField(null=True)
    description = models.TextField(max_length=400, null=True)
    requirements = models.TextField(max_length=500, null=False)
    is_available = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)