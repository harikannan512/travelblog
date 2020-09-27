"""travelblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as users_views
from bucketlist import views as bucketlist_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bucketlist/', include('bucketlist.urls')),
    path('bucketlist/home', bucketlist_views.home, name='home'),
    path('contact_us/', bucketlist_views.contact_us, name='contact_us'),
    path('new_post/', bucketlist_views.new_post, name='new_post'),
    path('bucketlist/<int:id>/<int:pid>/update/', bucketlist_views.update_post, name='update'),
    path('bucketlist/<int:id>/', bucketlist_views.continent_blog, name='continent_blog'),


    path('register/', users_views.register, name='register'),
    path('profile/', users_views.update_info, name='profile'),
    path('author/<int:id>', users_views.author, name='author'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
