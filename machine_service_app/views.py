from django.shortcuts import render
from rest_framework import generics

from machine_service_app.models import Machine
from .serializers import MachineSerializer


class MachineView(generics.CreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
