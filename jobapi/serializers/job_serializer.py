from rest_framework.serializers import ModelSerializer

from jobapi.entity.job_entity import JobEntity

class JobSerializer(ModelSerializer):
    class Meta:
        model = JobEntity
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True}
        }