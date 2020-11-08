from django.shortcuts import render
from rest_framework import generics
from home.models import Users
from .serializers import UsersSerializer

# Create your views here.

class UsersApiView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersApiViewDetails(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersApiNew(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer  

class UsersAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    print(queryset)
    serializer_class = UsersSerializer     

class UsersAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    

    