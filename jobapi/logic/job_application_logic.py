from jobapi.dao.job_application_dao import JobApplicationDao
from jobapi.dao.user_dao import UserDao

class JobApplicationLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_application_dao = JobApplicationDao()
        self.user_dao = UserDao()


    def job_apply(self, user, data, job, resume):
        user = self.user_dao.get_user(user.username)
        note = data.get('note')

        check_if_applied = self.job_application_dao.check_user_application(user, job)

        if check_if_applied:
            raise ValueError({"Message": "you have already applied to this job."})

        return self.job_application_dao.create_application(
            job=job,
            user=user,
            resume=resume,
            note=note
        )

    def get_all_job_applications(self, user):
        return self.job_application_dao.get_all_job_applications(user=user)