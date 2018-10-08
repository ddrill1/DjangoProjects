from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.lastName + ', ' + self.firstName
