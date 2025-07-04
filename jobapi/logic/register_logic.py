from rest_framework_simplejwt.tokens import RefreshToken
from jobapi.dao.user_dao import UserDao


class RegisterLogic:

    def __init__(self):
        self.user_dao = UserDao()

    def password_checker(self, username, password):

        user = self.user_dao.get_user(username)

        if not user:
            raise ValueError('User does not exist')

        return self.user_dao.password_checker(username, password)


    def generate_tokens(self, username):

        user = self.user_dao.get_user(username)

        if not user:
            raise ValueError('User does not exist')

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

