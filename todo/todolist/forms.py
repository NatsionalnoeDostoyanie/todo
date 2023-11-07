from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_complete']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название задачи', 'required': 'required'}),
            'description': forms.Textarea(attrs={'placeholder': 'Введите описание задачи', 'rows': 4, 'cols': 50}),
        }
