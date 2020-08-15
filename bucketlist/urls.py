from django.urls import path
from . import views

app_name = 'bucketlist'

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:country>/', views.country_blog, name='country_blog'),
    path('<str:country>/<int:id>/', views.article_page, name='article_page'),
    path('contact_us/', views.contact_us, name='contact-us'),
]
