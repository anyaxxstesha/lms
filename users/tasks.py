from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from users.models import User


@shared_task
def check_activity():
    """Если пользователь не заходил более месяца, то его аккаунт блокируется"""
    month_ago = timezone.now() - relativedelta(months=1)
    queryset = User.objects.filter(last_login__lt=month_ago, is_active=True)
    queryset.update(is_active=False)
