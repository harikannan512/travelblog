from django.urls import path
from . import views

app_name = 'bucketlist'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.continent_blog, name='continent_blog'),
    path('<int:id>/<int:pid>/', views.article_page, name='article_page'),
    path('<int:id>/<int:pid>/update', views.update_post, name='update'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('new_post/', views.new_post, name='new_post'),
    path('<int:id>/<int:pid>/delete', views.delete_post, name='delete')
]
