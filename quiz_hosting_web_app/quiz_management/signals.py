from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import QuizAttempter, Announcement


def send_username_password(email, username):
    subject = "Be ready for Quiz! "
    message = f'your username is {username} and password is namal123'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
    

@receiver(post_save, sender=QuizAttempter)
def send_email(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        username = instance.username
        send_username_password(email, username)

  
# def send_add_quiz_notification(email):
#     subject = "Added in another Quiz!"
#     message = f'Prepare and Attempt'
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)      
    
        
# @receiver(m2m_changed, sender=QuizAttempter.quiz_id.through)
# def quiz_attempter_quiz_changed(sender, instance, action, model, pk_set, **kwargs):
#     if action in ('post_add', 'post_remove', 'post_clear'):
#         send_add_quiz_notification(instance.email)
        

# @receiver(post_save, sender=Announcement)
# def send_email(sender, instance, created, **kwargs):
#     if created:
#         subject = instance.subject
#         details = instance.details
#         print(subject, details)
#         print(instance.quiz)
#         send_username_password(email, username)
    