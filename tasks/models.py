from django.db import models
from user.models import UserProfile
from .constants import  *

# Create your models here.
class Task(models.Model):
    STATUS=(
        (Status.PENDING,'PENDING'),
        (Status.IN_PROGRESS,'IN PROGRESS'),
        (Status.COMPLETED,'COMPLETED')
    )
    PRIORITY=(
        (Priority.HIGH,'HIGH'),
        (Priority.MEDIUM,'MEDIUM'),
        (Priority.LOW,'LOW')
    )
    title=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=500,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    priority=models.CharField(max_length=200,null=True,choices=PRIORITY)
    assigned_to=models.ForeignKey(UserProfile,null=True,blank=True,on_delete=models.SET_NULL)
    deadline=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title



