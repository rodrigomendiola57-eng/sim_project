from django.urls import path
from .views import (
    VehicleListView, VehicleCreateView, VehicleUpdateView, VehicleDeleteView, VehicleDetailView,
    DocumentListView, DocumentCreateView, DocumentUpdateView, DocumentDeleteView,
    MaintenanceListView, MaintenanceCreateView, MaintenanceUpdateView, MaintenanceDeleteView,
    MaintenanceTypeListView, MaintenanceTypeCreateView, MaintenanceTypeUpdateView, MaintenanceTypeDeleteView,
    MaintenanceBulkCreateView
)
from .views_dashboard import DashboardView
from .views_checklist import ChecklistListView, ChecklistCreateView, ChecklistDetailView, ChecklistDeleteView
from .views_pdf import MaintenancePDFView
from .views_documenttype import DocumentTypeListView, DocumentTypeCreateView, DocumentTypeUpdateView, DocumentTypeDeleteView
from .views_driver import DriverListView, DriverCreateView, DriverUpdateView, DriverDetailView, DriverDeleteView, DriverDocumentUploadView, DriverDocumentDeleteView
from .views_employee_documents import EmployeeDocumentsView
from .views_daily_report import DailyReportPDFView
from .views_workshop import WorkshopListView, WorkshopCreateView, WorkshopUpdateView, WorkshopDeleteView
from .views_maintenance_phases import MaintenanceDetailView, MaintenanceQuoteView, MaintenanceApproveView, MaintenanceRejectView, MaintenanceCompleteView
from .views_vehicle_documents import VehicleDocumentsView
from .views_qr_scanner import QRScannerView, QRLookupView
from .views_vehicle_pdf import VehiclePDFView
from .views_vehicle_advanced import (
    VehicleExportExcelView, VehicleExportPDFView, VehicleImportExcelView,
    VehicleHistoryView, VehicleQRCodeView, VehicleDownloadTemplateView
)

urlpatterns = [
    # ----------------- DASHBOARD -----------------
    path('', DashboardView.as_view(), name='dashboard'),
    path('daily-report/pdf/', DailyReportPDFView.as_view(), name='daily_report_pdf'),
    
    # ----------------- VEHICLES -----------------
    path('vehicles/', VehicleListView.as_view(), name='vehicle_list'),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicles/<int:pk>/history/', VehicleHistoryView.as_view(), name='vehicle_history'),
    path('vehicles/<int:pk>/qr/', VehicleQRCodeView.as_view(), name='vehicle_qr'),
    path('vehicles/<int:pk>/pdf/', VehiclePDFView.as_view(), name='vehicle_pdf'),
    path('vehicles/export/excel/', VehicleExportExcelView.as_view(), name='vehicle_export_excel'),
    path('vehicles/export/pdf/', VehicleExportPDFView.as_view(), name='vehicle_export_pdf'),
    path('vehicles/import/excel/', VehicleImportExcelView.as_view(), name='vehicle_import_excel'),
    path('vehicles/template/download/', VehicleDownloadTemplateView.as_view(), name='vehicle_download_template'),
    path('add/', VehicleCreateView.as_view(), name='vehicle_add'),
    path('update/<int:pk>/', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('delete/<int:pk>/', VehicleDeleteView.as_view(), name='vehicle_delete'),

    # ----------------- DOCUMENT TYPES -----------------
    path('document-types/', DocumentTypeListView.as_view(), name='documenttype_list'),
    path('document-types/add/', DocumentTypeCreateView.as_view(), name='documenttype_add'),
    path('document-types/update/<int:pk>/', DocumentTypeUpdateView.as_view(), name='documenttype_update'),
    path('document-types/delete/<int:pk>/', DocumentTypeDeleteView.as_view(), name='documenttype_delete'),

    # ----------------- DOCUMENTS -----------------
    path('documents/', DocumentListView.as_view(), name='document_list'),
    path('documents/add/', DocumentCreateView.as_view(), name='document_add'),
    path('documents/update/<int:pk>/', DocumentUpdateView.as_view(), name='document_update'),
    path('documents/delete/<int:pk>/', DocumentDeleteView.as_view(), name='document_delete'),
    path('documents/vehicles/', VehicleDocumentsView.as_view(), name='vehicle_documents'),
    path('documents/employees/', EmployeeDocumentsView.as_view(), name='employee_documents'),

    # ----------------- MAINTENANCE TYPES -----------------
    path('maintenance-types/', MaintenanceTypeListView.as_view(), name='maintenancetype_list'),
    path('maintenance-types/add/', MaintenanceTypeCreateView.as_view(), name='maintenancetype_add'),
    path('maintenance-types/update/<int:pk>/', MaintenanceTypeUpdateView.as_view(), name='maintenancetype_update'),
    path('maintenance-types/delete/<int:pk>/', MaintenanceTypeDeleteView.as_view(), name='maintenancetype_delete'),

    # ----------------- WORKSHOPS -----------------
    path('workshops/', WorkshopListView.as_view(), name='workshop_list'),
    path('workshops/add/', WorkshopCreateView.as_view(), name='workshop_add'),
    path('workshops/update/<int:pk>/', WorkshopUpdateView.as_view(), name='workshop_update'),
    path('workshops/delete/<int:pk>/', WorkshopDeleteView.as_view(), name='workshop_delete'),

    # ----------------- MAINTENANCE -----------------
    path('maintenance/', MaintenanceListView.as_view(), name='maintenance_list'),
    path('maintenance/add/', MaintenanceCreateView.as_view(), name='maintenance_add'),
    path('maintenance/bulk-add/', MaintenanceBulkCreateView.as_view(), name='maintenance_bulk_add'),
    path('maintenance/<int:pk>/', MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('maintenance/<int:pk>/quote/', MaintenanceQuoteView.as_view(), name='maintenance_quote'),
    path('maintenance/<int:pk>/approve/', MaintenanceApproveView.as_view(), name='maintenance_approve'),
    path('maintenance/<int:pk>/reject/', MaintenanceRejectView.as_view(), name='maintenance_reject'),
    path('maintenance/<int:pk>/complete/', MaintenanceCompleteView.as_view(), name='maintenance_complete'),
    path('maintenance/update/<int:pk>/', MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('maintenance/delete/<int:pk>/', MaintenanceDeleteView.as_view(), name='maintenance_delete'),
    path('maintenance/pdf/', MaintenancePDFView.as_view(), name='maintenance_pdf'),

    # ----------------- CHECKLISTS -----------------
    path('checklists/', ChecklistListView.as_view(), name='checklist_list'),
    path('checklists/create/', ChecklistCreateView.as_view(), name='checklist_create'),
    path('checklists/<int:pk>/', ChecklistDetailView.as_view(), name='checklist_detail'),
    path('checklists/<int:pk>/delete/', ChecklistDeleteView.as_view(), name='checklist_delete'),

    # ----------------- QR SCANNER -----------------
    path('qr/scanner/', QRScannerView.as_view(), name='qr_scanner'),
    path('qr/lookup/', QRLookupView.as_view(), name='qr_lookup'),
    
    # ----------------- DRIVERS -----------------
    path('drivers/', DriverListView.as_view(), name='driver_list'),
    path('drivers/create/', DriverCreateView.as_view(), name='driver_create'),
    path('drivers/<int:pk>/', DriverDetailView.as_view(), name='driver_detail'),
    path('drivers/<int:pk>/update/', DriverUpdateView.as_view(), name='driver_update'),
    path('drivers/<int:pk>/delete/', DriverDeleteView.as_view(), name='driver_delete'),
    path('drivers/<int:pk>/upload-document/', DriverDocumentUploadView.as_view(), name='driver_document_upload'),
    path('driver-documents/<int:pk>/delete/', DriverDocumentDeleteView.as_view(), name='driver_document_delete'),
]
