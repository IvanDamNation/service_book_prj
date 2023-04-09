from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from machine_service_app.models import Maintenance
from machine_service_app.permissions import IsAdminOrReadOnly
from machine_service_app.serializers import MaintenanceSerializer, ComplaintSerializer


# Maintenance
class MaintenanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Maintenance.objects.select_related(
        'type',
        'maintain_corp',
        'machine',
        'service_comp'
    ).all()
    serializer_class = MaintenanceSerializer
    permission_classes = (AllowAny, )


class MaintenanceSearchView(generics.RetrieveAPIView):
    queryset = Maintenance.objects.select_related(
        'type',
        'maintain_corp',
        'machine',
        'service_corp'
    ).all()
    serializer_class = MaintenanceSerializer
    permission_classes = (AllowAny,)


class MaintenanceGETListView(generics.ListAPIView):
    queryset = Maintenance.objects.select_related(
        'type',
        'maintain_corp',
        'machine',
        'service_comp'
    ).all()
    serializer_class = MaintenanceSerializer
    permission_classes = (AllowAny, )


class MaintenancePOSTView(generics.CreateAPIView):
    # permission_required = 'machine_service_app.add_maintenance'
    queryset = Maintenance.objects.select_related(
        'type',
        'maintain_corp',
        'machine',
        'service_comp'
    ).all()
    serializer_class = MaintenanceSerializer
    permission_classes = (IsAuthenticated, )


class MaintenancePUTView(generics.UpdateAPIView):
    # permission_required = 'machine_service_app.add_maintenance'
    queryset = Maintenance.objects.select_related(
        'type',
        'maintain_corp',
        'machine',
        'service_comp'
    ).all()
    serializer_class = MaintenanceSerializer
    permission_classes = (IsAuthenticated,)


class MaintenanceDestroyView(generics.UpdateAPIView):
    # permission_required = 'machine_service_app.add_maintenance'
    queryset = Maintenance.objects.select_related(
        'type',
        'maintain_corp',
        'machine',
        'service_comp'
    ).all()
    serializer_class = MaintenanceSerializer
    permission_classes = (IsAdminOrReadOnly, )


# Complaint
class ComplaintView(generics.CreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = ComplaintSerializer
