from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from jobapi.logic.sign_up_logic import SignUpLogic

class SignUpController(APIView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sign_up_logic = SignUpLogic()

    def post(self, request):
        try:
            data = request.data
            picture = data.get('picture')

            if not picture.name.lower().endswith('.jpg'):
                return Response("please upload valid .jpg file", HTTP_400_BAD_REQUEST)

            self.sign_up_logic.sign_up(data)
            return Response(None, HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)

