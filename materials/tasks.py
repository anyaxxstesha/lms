from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def start_mailshot(recipients: list):
    """Отправляет письма на указанные адреса"""
    send_mail('Изменения по Вашей подписке', 'Материалы курса обновились', settings.EMAIL_HOST_USER, recipients)
