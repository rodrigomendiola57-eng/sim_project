from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VehicleViewSet, DriverViewSet, MaintenanceViewSet,
    DocumentViewSet, ChecklistViewSet, WorkshopViewSet,
    MaintenanceTypeViewSet, DocumentTypeViewSet, DriverDocumentViewSet
)

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'drivers', DriverViewSet, basename='driver')
router.register(r'maintenances', MaintenanceViewSet, basename='maintenance')
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'checklists', ChecklistViewSet, basename='checklist')
router.register(r'workshops', WorkshopViewSet, basename='workshop')
router.register(r'maintenance-types', MaintenanceTypeViewSet, basename='maintenancetype')
router.register(r'document-types', DocumentTypeViewSet, basename='documenttype')
router.register(r'driver-documents', DriverDocumentViewSet, basename='driverdocument')

urlpatterns = [
    path('', include(router.urls)),
]
