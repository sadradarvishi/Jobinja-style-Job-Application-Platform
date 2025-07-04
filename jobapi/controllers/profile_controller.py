from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from jobapi.logic.profile_logic import ProfileLogic
from jobapi.serializers.user_serializer import UserSerializer

class ProfileController(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profile_logic = ProfileLogic()

    def get(self, request):
        try:
            user = request.user
            data = self.profile_logic.get_user(user)
            serialized_data = UserSerializer(data)
            return Response(serialized_data.data, HTTP_200_OK)
        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)


    def patch(self, request):
        try:
            user = request.user
            data = request.data
            self.profile_logic.edit_profile(data, user)

            return Response({"Message": "profile changed!"}, HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)

