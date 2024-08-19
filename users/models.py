from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Укажите почту')

    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='Телефон', help_text='Укажите телефон')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Город', help_text='Укажите город')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Аватар',
                               help_text='Загрузите аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']


PAYMENT_CHOICES = [
    ('tran', 'Перевод на счет'),
    ('cash', 'Наличными')
]


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='payments',
                             help_text='Укажите пользователя')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    course_paid = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Оплаченный курс',
                                    help_text='Укажите оплаченный курс', null=True, blank=True)
    lesson_paid = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Оплаченный урок',
                                    help_text='Укажите оплаченный урок', null=True, blank=True)
    payment_amount = models.FloatField(verbose_name='Сумма платежа', help_text='Укажите сумму платежа')
    payment_method = models.CharField(max_length=4, verbose_name='Способ оплаты', help_text='Укажите способ оплаты',
                                      choices=PAYMENT_CHOICES)
    session_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='id сессии',
                                  help_text='Укажите id сессии')
    link = models.URLField(max_length=400, blank=True, null=True, verbose_name='Ссылка на оплату',
                           help_text='Укажите ссылку на пользователя')

    def __str__(self):
        return f'{self.user.email} - {self.payment_amount} руб.'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='subscriptions',
                             help_text='Укажите пользователя')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс',
                               help_text='Укажите курс', related_name='subscriptions', null=True, blank=True)

    def __str__(self):
        return f'{self.user.email} - {self.course.title}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
