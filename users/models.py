from django.db import models
from django.contrib.auth.models import User
from .utils import pfp_image_url


class Bloguser(User):
    profile_pic = models.ImageField(upload_to=pfp_image_url(id), height_field=300, width_field=300, blank=True)

    def __str__(self):
        return self.username

    def register_user(self):
        User.objects.create_user(self.username, self.email, self.password)


class PostSubmission(models.Model):
    title = models.CharField(max_length=160)
    content = models.TextField()
    image_file = models.ImageField(upload_to='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
