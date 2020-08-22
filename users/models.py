from django.db import models
from django.contrib.auth.models import User


class Bloguser(User):
    username = User.username
    first = User.first_name
    last = User.last_name
    email = User.email
    password = User.password

    def register_user(self):
        User.objects.create_user(self.username, self.email, self.password)


class PostSubmission(models.Model):
    title = models.CharField(max_length=160)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
