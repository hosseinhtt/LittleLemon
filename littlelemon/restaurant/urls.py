from django.urls import path
from . import views

urlpatterns = [
    path('sayhello', views.say_hello, name='sayHello'),
    path('', views.index, name='index'),
]
