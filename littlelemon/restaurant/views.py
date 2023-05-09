from django.shortcuts import render, HttpResponse
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerilializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # search_fields = ['menu__title']
    # ordering_fields = ['price', 'inventory']

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


def say_hello(request):
    return HttpResponse('hello world')


def index(request):
    return render(request, 'index.html', {})
