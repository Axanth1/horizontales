from django.db import models

# Create your models here.

class Customer(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_phone = models.CharField(max_length=255)

    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        ordering = ['first_name']