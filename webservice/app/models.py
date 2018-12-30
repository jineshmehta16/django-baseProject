from django.db import models


class Roles(models.Model):
    roleId = models.IntegerField()
    roleName = models.CharField(max_length=20)

    def __str__(self):
        return self.roleName


class Users(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=30, blank=True)
    emailId = models.CharField(max_length=12,  blank=True)
    contactNumber = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=100, blank=True)
    userId = models.IntegerField()
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName

