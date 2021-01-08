from django.urls import path
from .views import base,createUser
urlpatterns = [
    path('',base),
    path('create-user',createUser),
]