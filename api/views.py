from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from vehicles.models import Vehicle, Driver, Maintenance, Document, VehicleChecklist, Workshop, MaintenanceType, DocumentType, DriverDocument
from .serializers import (
    VehicleSerializer, DriverSerializer, MaintenanceSerializer,
    DocumentSerializer, ChecklistSerializer, WorkshopSerializer,
    MaintenanceTypeSerializer, DocumentTypeSerializer, DriverDocumentSerializer
)
from datetime import date, timedelta

@method_decorator(csrf_exempt, name='dispatch')
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        total = self.queryset.count()
        active = self.queryset.filter(status='Active').count()
        maintenance = self.queryset.filter(status='Maintenance').count()
        return Response({
            'total': total,
            'active': active,
            'maintenance': maintenance
        })

@method_decorator(csrf_exempt, name='dispatch')
class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

@method_decorator(csrf_exempt, name='dispatch')
class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        pending = self.queryset.exclude(status='Completado')
        serializer = self.get_serializer(pending, many=True)
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    @action(detail=False, methods=['get'])
    def expired(self, request):
        today = date.today()
        expired = self.queryset.filter(expiry_date__lt=today)
        serializer = self.get_serializer(expired, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def expiring_soon(self, request):
        today = date.today()
        next_month = today + timedelta(days=30)
        expiring = self.queryset.filter(expiry_date__gte=today, expiry_date__lte=next_month)
        serializer = self.get_serializer(expiring, many=True)
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = VehicleChecklist.objects.all()
    serializer_class = ChecklistSerializer
    
    @action(detail=False, methods=['get'])
    def today(self, request):
        today = date.today()
        checklists = self.queryset.filter(inspection_date__date=today)
        serializer = self.get_serializer(checklists, many=True)
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer

@method_decorator(csrf_exempt, name='dispatch')
class MaintenanceTypeViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeSerializer

@method_decorator(csrf_exempt, name='dispatch')
class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

@method_decorator(csrf_exempt, name='dispatch')
class DriverDocumentViewSet(viewsets.ModelViewSet):
    queryset = DriverDocument.objects.all()
    serializer_class = DriverDocumentSerializer
