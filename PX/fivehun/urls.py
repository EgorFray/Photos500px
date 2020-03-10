from django.urls import path
from .views import *


urlpatterns = [
    path('', photo_list, name='photo_list_url'),
    path('post/<str:slug>/', photo_detail, name='photo_detail_url')
]