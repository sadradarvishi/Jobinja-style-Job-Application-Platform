from celery import shared_task
from django.core.mail import send_mail

from jobapi.entity.user_entity import UserEntity

@shared_task
def send_email(username):
    user = UserEntity.objects.get(username=username)
    subject = f"Hello {user.username}"
    message = (
        "Welcome to our platform\n\n"
        "We hope that you will find your dream job in our platform\n\n"
        "Wish you all the best!"
    )
    send_mail(
        subject=subject,
        message=message,
        from_email='sadsaddardar@gmail.com',
        recipient_list= [user.email],
        fail_silently=False
    )