from rest_framework import serializers

from machine_service_app.models import Machine, Maintenance, Complaint


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

        # fields = ('pk', 'factory_number', 'model',
        #           'engine', 'engine_num', 'transmission',
        #           'transmission_num', 'rear_axle', 'rear_axle_num',
        #           'front_axle', 'front_axle_num', 'supply_contract',
        #           'shipment_date', 'consignee', 'shipment_address',
        #           'equipment', 'client', 'service_comp')


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'
