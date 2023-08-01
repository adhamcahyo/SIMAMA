from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name

class Task(models.Model):
    CATEGORY_CHOICES = (
        ('IT', 'IT'),
        ('Pertanian', 'Pertanian'),
        ('Kedokteran', 'Kedokteran'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    reward = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    