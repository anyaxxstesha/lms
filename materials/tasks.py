from celery import shared_task
from django.core.mail import send_mail

from config import settings
from users.models import Subscription


@shared_task
def start_mailshot(course_id):
    """Отправляет письма на указанные адреса"""
    subscriptions = Subscription.objects.filter(course_id=course_id)
    subscribed_users = []
    for subscription in subscriptions:
        user = subscription.user
        subscribed_users.append(user.email)
    send_mail('Изменения по Вашей подписке', 'Материалы курса обновились', settings.EMAIL_HOST_USER, subscribed_users)
