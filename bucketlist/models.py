from django.db import models


# Create your models here
class Countries(models.Model):
    country_name = models.CharField(max_length=20)
    description = models.TextField()
    img_url = models.CharField(max_length=30, default='static/default.jpg')

    def __str__(self):
        return self.country_name

    def pic_url(self):
        return self.img_url
