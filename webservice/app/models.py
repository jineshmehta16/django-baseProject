from django.db import models

class Users(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=30)
    emailId = models.CharField(max_length=12)
    contactNumber = models.IntegerField()
    address = models.CharField(max_length=100)
    userId = models.IntegerField()

    def __str__(self):
        return self.firstName
