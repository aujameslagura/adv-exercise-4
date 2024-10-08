# articles/urls.py
from django.urls import path
from .views import TagListCreateView

urlpatterns = [
    path('api/articles/tags/', TagListCreateView.as_view(), name='tag-list-create'),
]
