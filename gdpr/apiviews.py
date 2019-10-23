from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
