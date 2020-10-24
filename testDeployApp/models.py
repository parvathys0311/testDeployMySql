import uuid

from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Function(models.Model):
    functionID = models.AutoField(primary_key = True)
    functionName = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.functionName


class Role(models.Model):
    roleID = models.AutoField(primary_key = True)
    roleName = models.CharField(max_length=200, default='')
    roleFunction = models.ForeignKey(Function,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.roleName

class Expert(models.Model):
    expertId = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=300, default='')
    email = models.EmailField(max_length=50,default='')
    expertiseFunction = models.ForeignKey(Function,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.firstName

class Candidate(models.Model):
    candidateId = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=300, default='')
    email = models.EmailField(max_length=50,default='')
    interestedRole = models.ForeignKey(Role,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.firstName