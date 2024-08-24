from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from users.models import User


@shared_task
def check_activity():
    """Если пользователь не заходил более месяца, то его аккаунт блокируется"""
    queryset = User.objects.all()
    for user in queryset:
        if user.last_login < (timezone.now() - timedelta(days=30)):
            user.is_active = False
            user.save()
