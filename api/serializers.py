from rest_framework import serializers
from vehicles.models import Vehicle, Driver, Maintenance, Document, VehicleChecklist, Workshop, MaintenanceType, DocumentType, DriverDocument

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source='vehicle.plate', read_only=True)
    maintenance_type_name = serializers.CharField(source='maintenance_type.name', read_only=True)
    workshop_name = serializers.CharField(source='workshop.name', read_only=True)
    
    class Meta:
        model = Maintenance
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source='vehicle.plate', read_only=True)
    doc_type_name = serializers.CharField(source='doc_type.name', read_only=True)
    is_expired = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Document
        fields = '__all__'

class ChecklistSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source='vehicle.plate', read_only=True)
    overall_status = serializers.CharField(read_only=True)
    
    class Meta:
        model = VehicleChecklist
        fields = '__all__'

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'

class MaintenanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceType
        fields = '__all__'

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'

class DriverDocumentSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(source='driver.full_name', read_only=True)
    driver_position = serializers.CharField(source='driver.position', read_only=True)
    
    class Meta:
        model = DriverDocument
        fields = '__all__'
