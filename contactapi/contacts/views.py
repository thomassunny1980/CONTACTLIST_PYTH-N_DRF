from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Contacts
from .serializers import ContactSerializer

# Create your views here.


class ContactList(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes =(permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def get_queryset(self):
        return Contacts.objects.filter(owner = self.request.user)
    

class ContactDetails(RetrieveUpdateDestroyAPIView):

    serializer_class =ContactSerializer
    permission_classes =(permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Contacts.objects.filter(owner= self.request.user)
    
