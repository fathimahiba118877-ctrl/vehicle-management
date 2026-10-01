from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'status', 'vehicle_type', 'service_type', 'estimated_cost')
    list_filter = ('status', 'vehicle_type', 'service_type')
    search_fields = ('description', 'customer_name', 'vehicle_number')
