from jobapi.dao.user_dao import UserDao


class ProfileLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_dao = UserDao()


    def get_user(self, user):
        username = user.username
        return self.user_dao.get_user(username)

    def edit_profile(self, data, user):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        phone_number = data.get('phone_number')
        experience = data.get('experience')
        education = data.get('education')
        return self.user_dao.edit_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
            phone_number=phone_number,
            experience=experience,
            education=education,
            user=user
        )
