from django.db import models


# Create your models here.
class Customer(models.Model):
    customerRequestId = models.CharField(max_length=40, null=True)
    customerName = models.CharField(max_length=40, null=True)
    customerEmailId = models.EmailField(blank=True, unique=True)
    customerMcafeeEmailId = models.EmailField(blank=True, unique=True)

    def __str__(self):
        return self.customerName