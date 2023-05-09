from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('sayhello', views.say_hello, name='sayHello'),
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu'),
    path('booking/', include(router.urls)),
]
