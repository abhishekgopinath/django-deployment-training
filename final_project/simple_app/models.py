from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    department = models.CharField(blank=False, max_length=50)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics')

    def __str__(self):
        return self.user.username
