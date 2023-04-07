from django.shortcuts import render
from rest_framework import generics

from machine_service_app.models import Machine, Maintenance
from .serializers import MachineSerializer, MaintenanceSerializer, ComplaintSerializer


class MachineGETView(generics.ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class MachinePOSTView(generics.ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class MaintenanceView(generics.CreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class ComplaintView(generics.CreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = ComplaintSerializer
