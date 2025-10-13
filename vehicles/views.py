from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vehicle, Document, Maintenance

# ----------------- VEHICLES -----------------
class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_list.html'

class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'vehicles/vehicle_form.html'
    fields = '__all__'
    success_url = reverse_lazy('vehicle_list')

class VehicleUpdateView(UpdateView):
    model = Vehicle
    template_name = 'vehicles/vehicle_form.html'
    fields = '__all__'
    success_url = reverse_lazy('vehicle_list')

class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'vehicles/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle_list')


# ----------------- DOCUMENTS -----------------
class DocumentListView(ListView):
    model = Document
    template_name = 'vehicles/document_list.html'

class DocumentCreateView(CreateView):
    model = Document
    template_name = 'vehicles/document_form.html'
    fields = '__all__'
    success_url = reverse_lazy('document_list')

class DocumentUpdateView(UpdateView):
    model = Document
    template_name = 'vehicles/document_form.html'
    fields = '__all__'
    success_url = reverse_lazy('document_list')

class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'vehicles/document_confirm_delete.html'
    success_url = reverse_lazy('document_list')


# ----------------- MAINTENANCE -----------------
class MaintenanceListView(ListView):
    model = Maintenance
    template_name = 'vehicles/maintenance_list.html'

class MaintenanceCreateView(CreateView):
    model = Maintenance
    template_name = 'vehicles/maintenance_form.html'
    fields = '__all__'
    success_url = reverse_lazy('maintenance_list')

class MaintenanceUpdateView(UpdateView):
    model = Maintenance
    template_name = 'vehicles/maintenance_form.html'
    fields = '__all__'
    success_url = reverse_lazy('maintenance_list')

class MaintenanceDeleteView(DeleteView):
    model = Maintenance
    template_name = 'vehicles/maintenance_confirm_delete.html'
    success_url = reverse_lazy('maintenance_list')
