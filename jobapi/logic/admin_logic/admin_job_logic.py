from jobapi.dao.job_dao import JobDao

class AdminJobLogic:

    def __init__(self):
        self.job_dao = JobDao()


    def create_job(self, data):
        return self.job_dao.create_job(
            company_name=data.get('company_name'),
            title=data.get('title'),
            location=data.get('location'),
            agreement=data.get('agreement'),
            salary=data.get('salary'),
            requirements=data.get('requirements'),
            description=data.get('description'),
            is_available=data.get('is_available', True)
        )

    def update_job(self, job_id, data):
        return self.job_dao.update_job(
            job_id=job_id,
            company_name=data.get('company_name'),
            title=data.get('title'),
            location=data.get('location'),
            agreement=data.get('agreement'),
            salary=data.get('salary'),
            requirements=data.get('requirements'),
            description=data.get('description'),
            is_available=data.get('is_available', True)
        )

    def query_by_company_and_title(self, company_name, title):
        return self.job_dao.query_by_company_and_title(company_name=company_name, title=title)

    def query_by_company_name(self, company_name):
        return self.job_dao.query_by_company_name(company_name=company_name)

    def query_by_title(self, title):
        return self.job_dao.query_by_title(title=title)

    def delete_event_by_id(self, job_id):
        return self.job_dao.delete_job_by_id(job_id)
