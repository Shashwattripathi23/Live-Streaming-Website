

# urls.py
from django.urls import path
from .views import index, video_feed

urlpatterns = [
    path('', index, name='index'),
    path('video_feed/<str:stream_key>/', video_feed, name='video_feed'),
]
