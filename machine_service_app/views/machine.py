from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from machine_service_app.models import Machine
from machine_service_app.permissions import IsAdminOrReadOnly
from machine_service_app.serializers import MachineSerializer


# main for GET
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
    permission_classes = (AllowAny,)


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
    permission_classes = (IsAuthenticated, )


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
    permission_classes = (IsAuthenticated, )


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
    permission_classes = (IsAdminOrReadOnly, )
