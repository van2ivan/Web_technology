from xml.dom import ValidationErr
from rest_framework import serializers
from contactbook_api.models import Contact
from django.forms import ValidationError
import datetime

class ContactSerializer(serializers.Serializer):

    nickname = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    phone_number = serializers.IntegerField()
    
    def save(self, **kwargs):
        contact = Contact.objects.create(nickname = self.data['nickname'], email=self.data['email'], phone_number=self.data['phone_number'], created_at=datetime.datetime.now())
        return contact

    def validate(self, data):
        if  len(data['nickname']) < 5:
            raise ValidationError("Thats a bad nickname. Ensure nickname has a minimum of 5 characters")
        return data