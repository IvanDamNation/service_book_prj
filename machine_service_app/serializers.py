from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from machine_service_app.models import Machine, Maintenance, Complaint, Dictionary


class MachineSerializer(serializers.ModelSerializer):
    model = serializers.CharField(source='model.machinemodel')
    engine = serializers.CharField(source='engine.enginemodel')
    transmission = serializers.CharField(source='transmission.transmissionmodel')
    rear_axle = serializers.CharField(source='rear_axle.rearaxlemodel')
    front_axle = serializers.CharField(source='front_axle.frontaxle')
    client = serializers.CharField(source='client.user')
    service_comp = serializers.CharField(source='service_comp.name')

    class Meta:
        model = Machine
        fields = ('pk', 'factory_number', 'model',
                  'engine', 'engine_num', 'transmission',
                  'transmission_num', 'rear_axle', 'rear_axle_num',
                  'front_axle', 'front_axle_num', 'supply_contract',
                  'shipment_date', 'consignee', 'shipment_address',
                  'equipment', 'client', 'service_comp')


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ('pk', 'type', 'date',
                  'operating_hours', 'work_order', 'work_order_date',
                  'maintain_corp', 'machine', 'service_comp')


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('date_of_complaint', 'operating_hours', 'unit_failure',
                  'failure_description', 'recovery_method', 'used_parts',
                  'date_of_repair', 'machine', 'service_comp')


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('name', 'description')
