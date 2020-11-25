from django.db import models
from users.models import Bloguser


class Continent(models.Model):
    continent_name = models.CharField(max_length=20)
    description = models.TextField()
    continent_img = models.ImageField(upload_to='continent_img/{id}', blank=False, default='default.jpg')

    def __str__(self):
        return self.continent_name

    def img_url(self):
        url = f'static/{self.continent_name}.jpg'
        return str(url)


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    pub_date = models.DateField()

    author = models.ForeignKey(Bloguser, on_delete=models.CASCADE)
    c_name = models.ForeignKey(Continent, on_delete=models.CASCADE)
