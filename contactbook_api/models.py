from django.db import models

class Contact(models.Model):
    nickname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.IntegerField(unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        contact = {"name": self.name, "number": self.phone_number}
        return contact