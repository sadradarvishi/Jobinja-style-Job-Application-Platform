from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED


from jobapi.dao.job_dao import JobDao
from jobapi.serializers.job_serializer import JobSerializer
from jobapi.logic.admin_logic.admin_job_logic import AdminJobLogic
from jobapi.permission import IsAdminUser


class AdminJobController(APIView):
    permission_classes = [IsAdminUser]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_dao = JobDao()
        self.admin_job_logic = AdminJobLogic()

    def get(self, request):
        try:
            data = request.query_params
            job_id = data.get('job_id')
            company_name = data.get('company_name')
            title = data.get('title')

            if job_id:
                if not job_id.isdigit():
                   return Response({"error": "id not valid"}, HTTP_400_BAD_REQUEST)
                data = self.job_dao.get_job_by_id(int(job_id))

                if not data:
                    return Response({"error": "no such id found"}, HTTP_400_BAD_REQUEST)
                serialized_data = JobSerializer(data)
                return Response(serialized_data.data, HTTP_200_OK)

            if company_name and title:
                jobs = self.admin_job_logic.query_by_company_and_title(company_name, title)
                serialized_data = JobSerializer(jobs, many=True)
                return Response(serialized_data.data, HTTP_200_OK)

            if company_name:
                data = self.admin_job_logic.query_by_company_name(company_name)
                serialized_data = JobSerializer(data, many=True)
                return Response(serialized_data.data, HTTP_200_OK)

            if title:
                data = self.admin_job_logic.query_by_title(title)
                serialized_data = JobSerializer(data, many=True)
                return Response(serialized_data.data, HTTP_200_OK)

            data = self.job_dao.get_all_jobs()
            serialized_data = JobSerializer(data, many=True)
            return Response(serialized_data.data, HTTP_200_OK)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            data = request.data
            self.admin_job_logic.create_job(data)
            return Response(data="job created", status=HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            data = request.data
            job_id = data.get('id')
            if not job_id:
                return Response({'error': 'enter an id'}, HTTP_400_BAD_REQUEST)
            job = self.job_dao.get_job_by_id(int(job_id))
            if not job:
                return Response({'error': 'could not find any job by this id'}, HTTP_400_BAD_REQUEST)
            self.admin_job_logic.update_job(job_id, data)
            return Response({'message': 'job updated'}, status=HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.query_params
            job_id = data.get('id')
            if not job_id:
                return Response({'error': 'no job found'}, HTTP_400_BAD_REQUEST)
            self.admin_job_logic.delete_event_by_id(int(job_id))
            return Response({'message': 'job deleted'}, HTTP_200_OK)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)
