from rest_framework import serializers

from users.models import Payments, User
from users.services import retrieve_stripe_status


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaymentsAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'
