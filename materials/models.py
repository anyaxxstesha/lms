from django.db import models

from config import settings


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Курс', help_text='Укажите название')
    preview_image = models.ImageField(upload_to='materials/course/', blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Укажите описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                              verbose_name='Создатель',
                              related_name='course', help_text='Укажите владельца курса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Урок', help_text='Укажите название')
    preview_image = models.ImageField(upload_to='materials/lesson/', blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Укажите описание')
    video_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на видео',
                                help_text='Укажите ссылку на видео')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True, related_name='lessons',
                               verbose_name='Курс',
                               help_text='Выберите курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                              verbose_name='Создатель',
                              related_name='lesson', help_text='Укажите владельца урока')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
