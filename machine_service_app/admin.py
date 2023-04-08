from django.contrib import admin

from machine_service_app.models import \
    Machine, Maintenance, Complaint, \
    Dictionary, MachineModel, EngineModel, \
    TransmissionModel, RearAxleModel, FrontAxle, \
    ServiceCompany


class MachineAdmin(admin.ModelAdmin):
    list_display = ('factory_number', 'model', 'supply_contract', 'client', )
    list_display_links = ('factory_number', 'client', )
    search_fields = ('factory_number', 'supply_contract', 'client', )
    list_filter = ('model', 'client', )


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('work_order', 'work_order_date', 'date',
                    'type', 'machine', 'maintain_corp',
                    'service_comp')
    list_display_links = ('work_order', 'service_comp', )
    search_fields = ('work_order', 'maintain_corp', 'service_comp', )
    list_filter = ('work_order_date', 'date', 'type',
                   'maintain_corp', 'service_comp', )


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('date_of_complaint', 'date_of_repair', 'machine',
                    'unit_failure', 'recovery_method', 'service_comp', )
    list_display_links = ('date_of_complaint', 'service_comp', )
    search_fields = ('machine', 'service_comp', )
    list_filter = ('date_of_complaint', 'recovery_method', 'service_comp', )


class DictionaryElementsAdmin(admin.ModelAdmin):
    list_display = ('type_dict', 'name', 'description', )
    list_display_links = ('name', 'description', )
    search_fields = ('name', 'description', )
    list_filter = ('name', 'description', )


class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    list_display_links = ('name', 'description', )
    search_fields = ('name', 'description', )
    list_filter = ('name', 'description', )


admin.site.register(Machine, MachineAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(ServiceCompany, ServiceCompanyAdmin)

# admin.site.register(Dictionary)

admin.site.register(MachineModel, DictionaryElementsAdmin)
admin.site.register(EngineModel, DictionaryElementsAdmin)
admin.site.register(TransmissionModel, DictionaryElementsAdmin)
admin.site.register(RearAxleModel, DictionaryElementsAdmin)
admin.site.register(FrontAxle, DictionaryElementsAdmin)
