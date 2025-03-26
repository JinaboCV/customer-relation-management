from django.db import models

class Record(models.Model):
    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=50)

    phone = models.CharField(max_length=21)

    address = models.CharField(max_length=80)

    city = models.CharField(max_length=255)

    province = models.CharField(max_length=300)

    country = models.CharField(max_length=50)

    creation_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.first_name + "   " + self.last_name

