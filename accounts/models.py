from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile (models.Model):
    USER_TYPE_CHOICES = [
        ('STU', 'STUDENT'),
        ('TEACH', 'TEACHER')
    ]
    user_type = models.CharField(
        'User type', choices=USER_TYPE_CHOICES, default='STU', max_length=5)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
