# todos/forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'is_resolved']
        # This dictionary controls how specific fields are rendered
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}), 
        }