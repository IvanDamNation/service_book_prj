from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from machine_service_app.models import Machine, Maintenance
from .permissions import IsAdminOrReadOnly
from .serializers import MachineSerializer, MaintenanceSerializer, ComplaintSerializer


class MachineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Machine.objects.select_related(
        'model',
        'engine',
        'transmission',
        'rear_axle',
        'front_axle',
        'client',
        'service_comp'
    ).all()
    serializer_class = MachineSerializer
    permission_classes = (AllowAny,)


class MachineSearchView(generics.RetrieveAPIView):
    queryset = Machine.objects.select_related(
        'model',
        'engine',
        'transmission',
        'rear_axle',
        'front_axle',
        'client',
        'service_comp'
    ).all()
    serializer_class = MachineSerializer


class MachineGETListView(generics.ListAPIView):
    queryset = Machine.objects.select_related(
        'model',
        'engine',
        'transmission',
        'rear_axle',
        'front_axle',
        'client',
        'service_comp'
    ).all()
    serializer_class = MachineSerializer
    permission_classes = (AllowAny,)


class MachinePOSTView(generics.CreateAPIView):
    # permission_required = 'machine_service_app.add_machine'
    queryset = Machine.objects.select_related(
        'model',
        'engine',
        'transmission',
        'rear_axle',
        'front_axle',
        'client',
        'service_comp'
    ).all()
    serializer_class = MachineSerializer


class MachinePUTView(generics.UpdateAPIView):
    # permission_required = 'machine_service_app.add_machine'
    queryset = Machine.objects.select_related(
        'model',
        'engine',
        'transmission',
        'rear_axle',
        'front_axle',
        'client',
        'service_comp'
    ).all()
    serializer_class = MachineSerializer


class MachineDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Machine.objects.select_related(
        'model',
        'engine',
        'transmission',
        'rear_axle',
        'front_axle',
        'client',
        'service_comp'
    ).all()
    serializer_class = MachineSerializer
    permission_classes = (IsAdminOrReadOnly,)


# Maintenance
class MaintenanceView(generics.CreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


# Complaint
class ComplaintView(generics.CreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = ComplaintSerializer
