from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from contactbook_api.models import Contact
from contactbook_api.serializer import ContactSerializer
from rest_framework.response import Response
from rest_framework import status

def contact_to_json(model):
    return {'nickname': model.nickname, 'email': model.email, 'phone_number': model.phone_number, 'created_at': model.created_at, 'id': model.id }

class ContactList(GenericAPIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


class ContactCreate(GenericAPIView):
    serializer_class = ContactSerializer
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(GenericAPIView):
    def getContactById(self, id):
        try:
            contact = Contact.objects.get(id=id)
            return contact
        except:
            return False
    def get(self, request, id):
        contact = self.getContactById(id)
        if not contact:
            return Response({
                'error': 'Contact not found'
            }, status=status.HTTP_404_NOT_FOUND)

        return Response(contact_to_json(contact))


class EditContact(GenericAPIView):
    serializer_class = ContactSerializer

    def getContactById(self, id):
        try:
            contact = Contact.objects.get(id=id)
            return contact
        except:
            return False

    def put(self, request, id):
        contact = self.getContactById(id)
        if not contact:
            return Response({
                'error': 'Contact not found'
            }, status=status.HTTP_404_NOT_FOUND)

        contact.nickname = request.data['nickname']
        contact.email = request.data['email']
        contact.phone_number = request.data['phone_number']
        contact.save()

        return Response(contact_to_json(contact))

class DeleteContact(GenericAPIView):
    def getContactById(self, id):
        try:
            contact = Contact.objects.get(id=id)
            return contact
        except:
            return False

    def delete(self, request, id):
        contact = self.getContactById(id)
        if not contact:
            return Response({
                'error': 'Contact not found'
            }, status=status.HTTP_404_NOT_FOUND)

        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)