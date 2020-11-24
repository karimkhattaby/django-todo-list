from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
        ('immediate', 'immediate'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title