from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    lesson_amount = SerializerMethodField()

    def get_lesson_amount(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lesson_amount')


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
