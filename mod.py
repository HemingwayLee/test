from django.db import models
from django.conf import settings

class UserProfile(models.Model):
  user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE)

  questions = models.CharField(max_length=1024)
  
