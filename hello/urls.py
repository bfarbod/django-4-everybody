from django.urls import path
from . import views

urlpatterns = [
    path('', views.cookies, name='hello_cookie')
]