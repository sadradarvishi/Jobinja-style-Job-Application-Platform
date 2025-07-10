from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from jobapi.dao.job_dao import JobDao
from jobapi.serializers.job_serializer import JobSerializer
from jobapi.logic.job_logic import JobLogic


class JobController(APIView, pagination.LimitOffsetPagination):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_logic = JobLogic()

    def get(self, request):
        try:
            data= request.query_params
            job_id = data.get('job_id')
            company_name = data.get('company_name')
            title = data.get('title')
            requirements = data.get('requirements')

            if company_name and title:
                jobs = self.job_logic.query_by_company_and_title(company_name, title)
                paginated_data = self.paginate_queryset(jobs, request, view=self)
                serialized_data = JobSerializer(paginated_data, many=True)
                return Response(serialized_data.data, HTTP_200_OK)

            if job_id:
                if not job_id.isdigit():
                    return Response({"error": "id not valid"}, HTTP_400_BAD_REQUEST)

                data = self.job_logic.get_job_by_id(int(job_id))
                if not data:
                    return Response({"error": "no jobs found by this id"}, HTTP_400_BAD_REQUEST)

                paginated_data = self.paginate_queryset(data, request, view=self)
                serialized_data = JobSerializer(paginated_data)
                return Response(serialized_data.data, HTTP_200_OK)

            if company_name:
                data = self.job_logic.query_by_company_name(company_name)
                paginated_data = self.paginate_queryset(data, request, view=self)
                serialized_data = JobSerializer(paginated_data, many=True)
                return Response(serialized_data.data, HTTP_200_OK)

            if title:
                data = self.job_logic.query_by_title(title)
                paginated_data = self.paginate_queryset(data, request, view=self)
                serialized_data = JobSerializer(paginated_data, many=True)
                return Response(serialized_data.data, HTTP_200_OK)

            if requirements:
                data = self.job_logic.query_by_requirements(requirements)
                paginated_data = self.paginate_queryset(data, request, view=self)
                serialized_data = JobSerializer(paginated_data, many=True)
                return Response(serialized_data.data, HTTP_200_OK)

            data = self.job_logic.get_all_jobs()
            paginated_data = self.paginate_queryset(data, request, view=self)
            serialized_data = JobSerializer(paginated_data, many=True)

            return Response(serialized_data.data, HTTP_200_OK)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)