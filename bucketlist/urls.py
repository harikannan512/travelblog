from django.urls import path
from . import views

app_name = 'bucketlist'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.country_blog, name='country_blog'),
    path('<int:id>/<int:pid>/', views.article_page, name='article_page'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
