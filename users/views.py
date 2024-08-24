from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from users.models import Payment, User, Subscription
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_stripe_price, create_stripe_session, get_or_create_stripe_product


class PaymentListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('payment_method', 'course_paid', 'lesson_paid')
    ordering_fields = ('date',)


class PaymentCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        amount = payment.payment_amount

        if payment.lesson_paid is not None:
            obj = payment.lesson_paid
        elif payment.course_paid is not None:
            obj = payment.course_paid
        else:
            return Response(data={'detail': 'lesson or course must be provided'}, status=status.HTTP_400_BAD_REQUEST)

        product = get_or_create_stripe_product(obj)
        price = create_stripe_price(amount, product)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()


class SubscriptionTogglerAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        course = get_object_or_404(Course, pk=pk)
        subscription, created = Subscription.objects.get_or_create(user=user, course=course)
        if created:
            return Response({"message": "subscription is added"}, status=status.HTTP_201_CREATED)
        else:
            subscription.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
