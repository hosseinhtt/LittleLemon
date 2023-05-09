from django.urls import path
from . import views

urlpatterns = [
    path('sayhello', views.say_hello, name='sayHello'),
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu'),
]
