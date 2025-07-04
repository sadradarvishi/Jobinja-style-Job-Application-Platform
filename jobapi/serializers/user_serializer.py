from rest_framework.serializers import ModelSerializer
from jobapi.entity.user_entity import UserEntity

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserEntity
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'phone_number',
                  'experience',
                  'education'
        ]
        extra_kwargs = {
            'id': {'read_only': True}
        }