from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    """Customer information."""

    name = models.TextField()
    last_name = models.TextField()
    tax_id = models.TextField(blank=True, default="C/F")
    address = models.TextField(blank=True, default="Ciudad")
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name + " " + self.last_name

