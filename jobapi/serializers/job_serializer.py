from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from jobapi.entity.job_entity import JobEntity

class JobSerializer(ModelSerializer):
    class Meta:
        model = JobEntity
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True}
        }


# class JobPaginatedSerializer(serializers.Serializer):
#     count = serializers.IntegerField()
#     next = serializers.CharField()
#     previous = serializers.CharField()
#     results = JobSerializer(many=True)