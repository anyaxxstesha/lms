from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault

from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
