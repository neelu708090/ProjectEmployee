from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    joining_date = models.DateField(default=timezone.now)
    description = models.TextField()
    employer= models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.first_name

    def get_absolute_url(self):
        return reverse('Home')

