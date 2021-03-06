from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('channels', views.get_channels),
    path('channels/add', views.add_channels),
    path('feeds', views.get_feeds),
]
