from rest_framework.fields import SerializerMethodField, URLField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from materials.validators import validate_url


class LessonSerializer(ModelSerializer):
    video_url = URLField(validators=[validate_url])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lesson_amount = SerializerMethodField()

    def get_lesson_amount(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lesson_amount')


class DetailCourseSerializer(CourseSerializer):
    lessons = LessonSerializer(many=True, source='lessons.all', read_only=True)
    is_user_subscribed = SerializerMethodField()

    def get_is_user_subscribed(self, obj):
        user = self.context['request'].user
        return obj.subscriptions.filter(user=user).exists()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lesson_amount', 'lessons', 'is_user_subscribed')
