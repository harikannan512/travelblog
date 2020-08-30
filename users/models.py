from django.db import models
from django.contrib.auth.models import User


class Bloguser(User):
    profile_pic = models.ImageField(upload_to=f'profile_pic/{id}', blank=True, default='default.jpg')

    def __str__(self):
        return self.username

    def register_user(self):
        User.objects.create_user(self.username, self.email, self.password)
