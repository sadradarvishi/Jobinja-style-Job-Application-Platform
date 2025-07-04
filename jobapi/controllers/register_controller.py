from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED

from jobapi.logic.register_logic import RegisterLogic

class RegisterController(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_logic = RegisterLogic()

    def post(self, request):
        try:
            data = request.data
            username = data.get("username")
            password = data.get("password")
            if not username:
                return Response({'error': 'enter username'}, HTTP_400_BAD_REQUEST)

            if not password:
                return Response({'error': 'enter password'}, HTTP_400_BAD_REQUEST)

            password_validation = self.register_logic.password_checker(username, password)

            if not password_validation:
                return Response({'error': 'password is incorrect'}, HTTP_400_BAD_REQUEST)

            tokens = self.register_logic.generate_tokens(username)

            return Response(tokens, HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)