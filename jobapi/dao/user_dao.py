from jobapi.entity.user_entity import UserEntity

from typing import Optional

class UserDao:

    def get_user(self, username):
        return UserEntity.objects.get(username=username)

    def password_checker(self, username, password):
        return UserEntity.objects.filter(username=username, password=password).exists()

    def create_user(
            self,
            first_name,
            last_name,
            username,
            password,
            email,
            experience,
            phone_number,
            education
    ):
        return UserEntity.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
            experience=experience,
            phone_number=phone_number,
            education=education
        )

    def edit_user(
            self,
            user,
            first_name: Optional[str],
            last_name: Optional[str],
            username: Optional[str],
            password: Optional[str],
            email: Optional[str],
            phone_number: Optional[str],
            experience: Optional[str],
            education: Optional[str],
    ):
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if username:
            user.username = username
        if password:
            user.set_password(password)
        if email:
            user.email = email
        if phone_number:
            user.phone_number = phone_number
        if experience:
            user.experience = experience
        if education:
            user.education = education

        user.save()
        return user


