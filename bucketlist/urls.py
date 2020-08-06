from django.urls import path
from . import views

app_name = 'bucketlist'

urlpatterns = [
    path('', views.home, name='home'),
]
