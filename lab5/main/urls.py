from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, ),
    path('get/names/<max_id>', views.get_names),
    path('get/photo/<max_id>', views. get_photo),
]
