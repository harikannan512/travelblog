from django.db import models


class Countries(models.Model):
    country_name = models.CharField(max_length=20)
    description = models.TextField()
    img_url = models.CharField(max_length=30, default='static/default.jpg')

    def __str__(self):
        return self.country_name

    def pic_url(self):
        return self.img_url


class CountryPage(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    pub_date = models.DateField()

    c_name = models.ForeignKey(Countries, on_delete=models.CASCADE)
