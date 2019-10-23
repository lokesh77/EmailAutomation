from rest_framework import serializers
from .models import Customer
from django.core.mail import send_mail
from django.conf import settings


def email(email1, email2, name, id):
    subject = 'Thank you for registering to our site'
    message = """\
    Dear {name},
            This email is in response to your recent information request via our web based form. We have received your Individual Data Request and assigned the following request number [{id}]. We will use this request number to track your data request through our system.
    As part of the identity verification process, you may receive additional communications from us within the next 5 business days. We will respond to your Individual Data Request within 30 days of this acknowledgement email.
    Thank you.
    Regards,
    McAfee Data Subject Rights (DSR) Operations
    Gdpr_request@mcafee.com
            
    """.format(name=name, id=id)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email1, email2]
    send_mail(subject, message, email_from, recipient_list)
    return "email sent successfully"


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customerRequestId', 'customerName', 'customerEmailId', 'customerMcafeeEmailId')

    def create(self, validated_data):
        customer = Customer(**validated_data)
        customer.save()
        Customer.objects.get_or_create(**validated_data)
        input_customerEmailId = validated_data.__getitem__('customerEmailId')
        print(input_customerEmailId)
        input_customerMcafeeEmailId = validated_data.__getitem__('customerMcafeeEmailId')
        print(input_customerMcafeeEmailId)
        input_customerRequestId = validated_data.__getitem__('customerRequestId')
        print(input_customerRequestId)
        input_customerName = validated_data.__getitem__('customerName')
        print(input_customerName)
        email(input_customerEmailId, input_customerMcafeeEmailId, input_customerName, input_customerRequestId)
        return customer