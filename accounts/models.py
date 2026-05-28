from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=11) 

    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user}'
    