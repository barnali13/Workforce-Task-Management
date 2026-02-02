from django.forms import ModelForm
from django import forms
from .models import Task
class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields='__all__'
        exclude=['created_at','updated_at']
        widgets={
            "deadline":forms.DateInput(
                attrs={"type":"date"}
            )
        }
class TaskStatusUpdateForm(ModelForm):
    class Meta:
        model=Task
        fields=['status']