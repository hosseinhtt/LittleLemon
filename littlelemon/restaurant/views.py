from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import Group, User
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


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
