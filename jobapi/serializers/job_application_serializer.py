from rest_framework.serializers import ModelSerializer

from jobapi.entity.job_application_entity import JobApplicationEntity

class JobApplicationSerializer(ModelSerializer):
    class Meta:
        Model = JobApplicationEntity
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True}
        }