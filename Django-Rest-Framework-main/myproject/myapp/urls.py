# myapp/urls.py
from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),  # Include articles URLs
]
