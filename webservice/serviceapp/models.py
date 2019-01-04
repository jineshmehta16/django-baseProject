from django.db import models
from enum import Enum


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


class CallStatus(Enum):
    NON_QUALIFIED = "Non Qualified"
    COLD_CALL = "Cold Call"
    QUALIFIED_CALL = "Qualified Call"
    WARM_CALL = "Warm Call"
    HOT_CALL = "Hot Call"
    CONVERTED = "Converted"


class Leads(models.Model):
    leadId = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=30, blank=True)
    emailId = models.CharField(max_length=12,  blank=True)
    contactNumber = models.CharField(max_length=12)
    address = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100)
    remarks = models.CharField(max_length=500)
    assignedTo = models.ForeignKey(Users, on_delete=models.CASCADE)
    callStatus = models.CharField(
      max_length=25,
      default=CallStatus.QUALIFIED_CALL,
      choices=[(eachCall.name, eachCall.value) for eachCall in CallStatus]  # Choices from Enum created above
    )

    def __str__(self):
        return self.firstName

