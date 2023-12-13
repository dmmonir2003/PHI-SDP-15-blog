
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/',include('author.urls')),
    path('categories/',include('categories.urls')),
    path('posts/',include('posts.urls')),
    path('profiles/',include('profiles.urls')),
]
