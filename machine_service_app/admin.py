from django.contrib import admin

from machine_service_app.models import Machine, Maintenance, Complaint


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'author', 'title', 'category', 'created_at', 'updated_at', 'is_published')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'author', 'content')
#     list_editable = ('is_published', )
#     list_filter = ('is_published', 'category')


class MachineAdmin(admin.ModelAdmin):
    list_display = ('factory_number', 'model', 'supply_contract', 'client', )
    list_display_links = ('factory_number', 'client', )
    search_fields = ('factory_number', 'supply_contract', 'client', )
    list_filter = ('model', 'client', )

# Maintenance
# Complaint
# Dictionary?


admin.site.register(Machine, MachineAdmin)
# admin.site.register(Maintenance, MaintenanceAdmin)
# admin.site.register(Complaint, ComplaintAdmin)
