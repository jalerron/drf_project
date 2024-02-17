from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics

from users.models import Payments
from users.serializers import PaymentsListAPISerializer


# Create your views here.
class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsListAPISerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_lesson', 'paid_course', 'paid_method')
    ordering_fields = ['date_payments']
