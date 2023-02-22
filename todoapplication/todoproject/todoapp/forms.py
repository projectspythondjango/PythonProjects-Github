from django import forms
from .models import Task
class ToDoForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']