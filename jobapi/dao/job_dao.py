from jobapi.entity.job_entity import JobEntity
from typing import Optional

class JobDao:
    model_class = JobEntity

    def create_job(
            self,
            company_name: str,
            title: str,
            location: str,
            agreement: str,
            salary: Optional[int],
            requirements: str,
            description: Optional[str] = None,
            is_available: bool = True
    ):
        return JobEntity.objects.create(
            company_name=company_name,
            title=title,
            location = location,
            agreement=agreement,
            salary=salary,
            requirements=requirements,
            description=description,
            is_available=is_available
        )

    def get_all_jobs(self):
        return JobEntity.objects.filter(is_deleted=False)

    def get_job_by_id(self, job_id: int):
        return JobEntity.objects.get(id=job_id, is_deleted=False)

    def update_job(
            self,
            job_id: int,
            company_name: Optional[str],
            title: Optional[str],
            location: Optional[str],
            agreement: Optional[str],
            salary: Optional[int],
            requirements: Optional[str],
            description: Optional[str],
            is_available: Optional[bool],
    ) -> Optional[JobEntity]:
        job = JobEntity.objects.filter(id=job_id, is_deleted=False).first()
        if not job:
            return None

        if company_name is not None:
            job.company_name = company_name
        if title is not None:
            job.title = title
        if location:
            job.location = location
        if agreement is not None:
            job.agreement = agreement
        if salary is not None:
            job.salary = salary
        if requirements is not None:
            job.requirements = requirements
        if description is not None:
            job.description = description
        if is_available is not None:
            job.is_available = is_available

        job.save()

    def delete_job_by_id(self, job_id):
        job = self.get_job_by_id(job_id)
        job.is_deleted = True

        job.save()

    def query_by_company_and_title(self, company_name, title):
        return JobEntity.objects.filter(
            company_name__icontains=company_name,
            title__icontains=title,
            is_deleted=False
        ).order_by('-created_at')

    def query_by_company_name(self, company_name):
        return JobEntity.objects.filter(
            company_name__icontains=company_name,
            is_deleted=False
        ).order_by('-created_at')

    def query_by_title(self, title):
        return JobEntity.objects.filter(
            title__icontains=title,
            is_deleted=False
        ).order_by('-created_at')

    def query_by_requirements(self, requirements):
        return JobEntity.objects.filter(
            requirements__icontains=requirements,
            is_deleted=False
        ).order_by('-created_at')
