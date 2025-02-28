 # myapp/tasks.py

from django.core.mail import send_mail
from django.conf import settings

def send_notification_email(user_email):
    subject = 'Напоминание о записи настроения'
    message = 'Не забудьте записать свое настроение!'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])
    
