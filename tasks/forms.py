from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'category']
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            categories = Category.objects.filter(owner=user)
            if len(categories) == 0:
                instance = CategoryForm().save(commit=False)
                instance.name = 'Uncategorized'
                instance.owner = user
                instance.save()
                categories = Category.objects.filter(owner=user)
            self.fields['category'].queryset = categories
