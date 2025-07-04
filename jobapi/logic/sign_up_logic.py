from jobapi.dao.user_dao import UserDao

class SignUpLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_dao = UserDao()

    def sign_up(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        experience = data.get('experience')
        phone_number = data.get('phone_number')
        education = data.get('education')
        return self.user_dao.create_user(
            first_name,
            last_name,
            username,
            password,
            email,
            experience,
            phone_number,
            education
        )
