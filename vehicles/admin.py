from django.contrib import admin
from .models import Vehicle, Document, Maintenance, MaintenanceType, VehicleChecklist, DocumentType, Driver, DriverDocument, Workshop

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['plate', 'brand', 'model', 'year', 'status', 'created_at']
    list_filter = ['status', 'brand', 'year']
    search_fields = ['plate', 'brand', 'model']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'validity_months', 'is_required', 'description']
    list_filter = ['is_required']
    search_fields = ['name']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['doc_type', 'vehicle', 'issue_date', 'expiry_date', 'is_expired']
    list_filter = ['doc_type', 'expiry_date']
    search_fields = ['vehicle__plate', 'doc_type__name', 'document_number']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(MaintenanceType)
class MaintenanceTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'estimated_cost', 'description']
    search_fields = ['name']

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address']
    search_fields = ['name', 'phone']

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['maintenance_type', 'vehicle', 'status', 'detection_date', 'workshop', 'estimated_cost', 'cost']
    list_filter = ['status', 'maintenance_type', 'workshop', 'detection_date']
    search_fields = ['vehicle__plate', 'maintenance_type__name', 'workshop__name', 'detected_by']
    readonly_fields = ['created_at', 'updated_at', 'detection_date']

@admin.register(VehicleChecklist)
class VehicleChecklistAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'driver_name', 'inspection_date', 'overall_status', 'odometer_reading']
    list_filter = ['inspection_date']
    search_fields = ['vehicle__plate', 'driver_name']
    readonly_fields = ['inspection_date']

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'phone', 'license_number', 'license_expiry', 'status', 'hire_date']
    list_filter = ['status', 'position', 'hire_date']
    search_fields = ['full_name', 'phone', 'license_number', 'position']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(DriverDocument)
class DriverDocumentAdmin(admin.ModelAdmin):
    list_display = ['driver', 'document_type', 'upload_date']
    list_filter = ['document_type', 'upload_date']
    search_fields = ['driver__full_name', 'description']
    readonly_fields = ['upload_date']
