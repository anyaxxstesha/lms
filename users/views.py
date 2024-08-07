from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('payment_method', 'course_paid', 'lesson_paid')
    ordering_fields = ('date',)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
