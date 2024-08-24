from rest_framework.serializers import ValidationError

approved_words = ['youtube.com', 'www.youtube.com']


def validate_url(url):
    domain = url.split('//')[1].split('/')[0]
    if domain not in approved_words:
        raise ValidationError("В материалах урока могут содержаться только видео с платформы YouTube")
