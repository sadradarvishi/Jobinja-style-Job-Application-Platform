from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK

from jobapi.logic.job_application_logic import JobApplicationLogic
from jobapi.dao.job_dao import JobDao
from jobapi.serializers.job_application_serializer import JobApplicationSerializer
from jobapi.serializers.job_serializer import JobSerializer

class JobApplicationController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_application_logic = JobApplicationLogic()
        self.job_dao = JobDao()


    def get(self, request):
        try:
            user = request.user
            applications = self.job_application_logic.get_all_job_applications(user)
            jobs = [app.job for app in applications]

            serialized_data= JobSerializer(jobs, many=True)
            return Response(serialized_data.data, HTTP_200_OK)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            user = request.user
            data = request.data
            resume = request.FILES.get('resume')
            job = self.job_dao.get_job_by_id(data.get('job_id'))

            if not job:
                raise ValueError({'Message': 'there is no job with this id'})

            self.job_application_logic.job_apply(user, data, job, resume)

            return Response({"Message": "Application submitted successfully"}, HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)


