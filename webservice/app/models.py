from django.db import models

class Users(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName