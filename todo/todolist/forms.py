from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = ['title', 'description', 'status', 'date_postponed', ]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Введите название задачи',
                    'required': 'required',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Введите описание задачи',
                    'rows': 4, 'cols': 50
                }
            ),

            'status': forms.Select(
                attrs={
                    'onchange': 'toggleDateField(this);',
                }
            ),

            'date_postponed': forms.DateTimeInput(
                attrs={
                    'style': 'display: none'
                }
            ),
        }
