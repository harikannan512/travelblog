from django.db import models
from users.models import Bloguser


class Continent(models.Model):
    continent_name = models.CharField(max_length=20)
    description = models.TextField()
    img_url = models.CharField(max_length=30, default='static/default.jpg')

    def __str__(self):
        return self.continent_name

    def pic_url(self):
        return self.img_url


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    pub_date = models.DateField()

    author = models.ForeignKey(Bloguser, on_delete=models.CASCADE)
    c_name = models.ForeignKey(Continent, on_delete=models.CASCADE)
