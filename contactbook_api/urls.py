from django.contrib import admin
from django.urls import path
from contactbook_api.views import ContactList, ContactDetail, ContactCreate, EditContact, DeleteContact

urlpatterns = [
    path('list/', ContactList.as_view()),
    path('create/', ContactCreate.as_view()),
    path('<int:id>', ContactDetail.as_view()),
    path('update/<int:id>', EditContact.as_view()),
    path('delete/<int:id>', DeleteContact.as_view())
]