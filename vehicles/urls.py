from django.urls import path
from . import views

urlpatterns = [
    # ---------- VEHICLES ----------
    path('vehicles/', views.VehicleListView.as_view(), name='vehicle_list'),
    path('vehicles/add/', views.VehicleCreateView.as_view(), name='vehicle_add'),
    path('vehicles/<int:pk>/edit/', views.VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('vehicles/<int:pk>/delete/', views.VehicleDeleteView.as_view(), name='vehicle_delete'),

    # ---------- DOCUMENTS ----------
    path('documents/', views.DocumentListView.as_view(), name='document_list'),
    path('documents/add/', views.DocumentCreateView.as_view(), name='document_add'),
    path('documents/<int:pk>/edit/', views.DocumentUpdateView.as_view(), name='document_edit'),
    path('documents/<int:pk>/delete/', views.DocumentDeleteView.as_view(), name='document_delete'),

    # ---------- MAINTENANCE ----------
    path('maintenance/', views.MaintenanceListView.as_view(), name='maintenance_list'),
    path('maintenance/add/', views.MaintenanceCreateView.as_view(), name='maintenance_add'),
    path('maintenance/<int:pk>/edit/', views.MaintenanceUpdateView.as_view(), name='maintenance_edit'),
    path('maintenance/<int:pk>/delete/', views.MaintenanceDeleteView.as_view(), name='maintenance_delete'),
]

