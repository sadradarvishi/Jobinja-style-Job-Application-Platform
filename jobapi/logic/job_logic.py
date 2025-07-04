from jobapi.dao.job_dao import JobDao


class JobLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_dao = JobDao()

    def get_job_by_id(self, job_id):
        return self.job_dao.get_job_by_id(job_id=job_id)

    def get_all_jobs(self):
        return self.job_dao.get_all_jobs()

    def query_by_company_and_title(self, company_name, title):
        return self.job_dao.query_by_company_and_title(company_name=company_name, title=title)

    def query_by_company_name(self, company_name):
        return self.job_dao.query_by_company_name(company_name=company_name)

    def query_by_title(self, title):
        return self.job_dao.query_by_title(title=title)

    def query_by_requirements(self, requirements):
        return self.job_dao.query_by_requirements(requirements=requirements)