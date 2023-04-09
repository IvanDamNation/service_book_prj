from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from machine_service_app.models import Maintenance
from machine_service_app.permissions import IsAdminOrReadOnly
from machine_service_app.serializers import ComplaintSerializer


# main for GET
class ComplaintViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Maintenance.objects.select_related(
        'unit_failure',
        'recovery_method',
        'machine',
        'service_comp'
    ).all()
    serializer_class = ComplaintSerializer
    permission_classes = (AllowAny, )


class ComplaintSearchView(generics.RetrieveAPIView):
    queryset = Maintenance.objects.select_related(
        'unit_failure',
        'recovery_method',
        'machine',
        'service_comp'
    ).all()
    serializer_class = ComplaintSerializer
    permission_classes = (AllowAny, )


class ComplaintGETListView(generics.ListAPIView):
    queryset = Maintenance.objects.select_related(
        'unit_failure',
        'recovery_method',
        'machine',
        'service_comp'
    ).all()
    serializer_class = ComplaintSerializer
    permission_classes = (AllowAny,)


class ComplaintPOSTView(generics.CreateAPIView):
    # permission_required = 'machine_service_app.add_complaint'
    queryset = Maintenance.objects.select_related(
        'unit_failure',
        'recovery_method',
        'machine',
        'service_comp'
    ).all()
    serializer_class = ComplaintSerializer
    permission_classes = (IsAuthenticated,)


class ComplaintPUTView(generics.UpdateAPIView):
    # permission_required = 'machine_service_app.add_complaint'
    queryset = Maintenance.objects.select_related(
        'unit_failure',
        'recovery_method',
        'machine',
        'service_comp'
    ).all()
    serializer_class = ComplaintSerializer
    permission_classes = (IsAuthenticated,)


class ComplaintDestroyView(generics.RetrieveDestroyAPIView):
    # permission_required = 'machine_service_app.add_complaint'
    queryset = Maintenance.objects.select_related(
        'unit_failure',
        'recovery_method',
        'machine',
        'service_comp'
    ).all()
    serializer_class = ComplaintSerializer
    permission_classes = (IsAdminOrReadOnly, )
