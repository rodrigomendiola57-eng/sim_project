from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from .models import Vehicle, Document, Maintenance, MaintenanceType, Workshop
from .forms import VehicleForm, DocumentForm, MaintenanceForm

# ----------------- VEHICLES -----------------
class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_list_new.html'
    context_object_name = 'vehicles'
    paginate_by = 50

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        
        # Búsqueda general
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(plate__icontains=search) |
                Q(brand__icontains=search) |
                Q(model__icontains=search) |
                Q(year__icontains=search)
            )
        
        # Filtro por estación
        station = self.request.GET.get('station')
        if station:
            queryset = queryset.filter(station=station)
        
        # Filtro por estado
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        # Filtro por año
        year = self.request.GET.get('year')
        if year:
            queryset = queryset.filter(year=year)
        
        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class VehicleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'vehicles.add_vehicle'
    raise_exception = False
    permission_denied_message = 'No tienes permisos para crear vehículos'
    model = Vehicle
    
    def handle_no_permission(self):
        messages.error(self.request, 'No tienes permisos para crear vehículos')
        return redirect('vehicle_list')
    form_class = VehicleForm
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self, form):
        messages.success(self.request, 'Vehículo creado exitosamente')
        return super().form_valid(form)

class VehicleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'vehicles.change_vehicle'
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self, form):
        messages.success(self.request, 'Vehículo actualizado exitosamente')
        return super().form_valid(form)

class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'vehicles/vehicle_detail.html'
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Document.objects.filter(vehicle=self.object).select_related('doc_type')
        context['maintenances'] = Maintenance.objects.filter(vehicle=self.object).select_related('maintenance_type', 'workshop').order_by('-created_at')[:10]
        from .models import VehicleChecklist
        context['checklists'] = VehicleChecklist.objects.filter(vehicle=self.object).order_by('-inspection_date')[:10]
        return context

class VehicleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'vehicles.delete_vehicle'
    model = Vehicle
    template_name = 'vehicles/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Vehículo eliminado exitosamente')
        return super().delete(request, *args, **kwargs)


# ----------------- DOCUMENTS -----------------
class DocumentListView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'vehicles/document_list.html'
    context_object_name = 'documents'
    paginate_by = 10

    def get_queryset(self):
        return Document.objects.select_related('vehicle').all()

class DocumentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'vehicles.add_document'
    model = Document
    form_class = DocumentForm
    template_name = 'vehicles/document_form.html'
    success_url = reverse_lazy('vehicle_documents')

    def get_initial(self):
        initial = super().get_initial()
        vehicle_id = self.request.GET.get('vehicle')
        if vehicle_id:
            initial['vehicle'] = vehicle_id
        return initial

    def form_valid(self, form):
        messages.success(self.request, 'Documento creado exitosamente')
        return super().form_valid(form)

class DocumentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'vehicles.change_document'
    model = Document
    form_class = DocumentForm
    template_name = 'vehicles/document_form.html'
    success_url = reverse_lazy('document_list')

    def form_valid(self, form):
        messages.success(self.request, 'Documento actualizado exitosamente')
        return super().form_valid(form)

class DocumentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'vehicles.delete_document'
    model = Document
    template_name = 'vehicles/document_confirm_delete.html'
    success_url = reverse_lazy('document_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Documento eliminado exitosamente')
        return super().delete(request, *args, **kwargs)


# ----------------- MAINTENANCE -----------------
class MaintenanceListView(LoginRequiredMixin, ListView):
    model = Maintenance
    template_name = 'vehicles/maintenance_list.html'
    context_object_name = 'maintenances'
    paginate_by = 10

    def get_queryset(self):
        queryset = Maintenance.objects.select_related('vehicle', 'maintenance_type', 'workshop').all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(vehicle__plate__icontains=search) |
                Q(vehicle__brand__icontains=search) |
                Q(vehicle__model__icontains=search) |
                Q(maintenance_type__name__icontains=search) |
                Q(workshop__name__icontains=search) |
                Q(detected_by__icontains=search)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class MaintenanceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'vehicles.add_maintenance'
    model = Maintenance
    template_name = 'vehicles/maintenance_form.html'
    fields = ['vehicle', 'maintenance_type', 'detected_by', 'problem_description']
    success_url = reverse_lazy('maintenance_list')

    def form_valid(self, form):
        form.instance.status = 'Detectado'
        messages.success(self.request, 'Problema detectado y registrado exitosamente')
        return super().form_valid(form)

class MaintenanceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'vehicles.change_maintenance'
    model = Maintenance
    form_class = MaintenanceForm
    template_name = 'vehicles/maintenance_form.html'
    success_url = reverse_lazy('maintenance_list')

    def form_valid(self, form):
        messages.success(self.request, 'Mantenimiento actualizado exitosamente')
        return super().form_valid(form)

class MaintenanceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'vehicles.delete_maintenance'
    model = Maintenance
    template_name = 'vehicles/maintenance_confirm_delete.html'
    success_url = reverse_lazy('maintenance_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Mantenimiento eliminado exitosamente')
        return super().delete(request, *args, **kwargs)


# ----------------- MAINTENANCE TYPES -----------------
class MaintenanceTypeListView(LoginRequiredMixin, ListView):
    model = MaintenanceType
    template_name = 'vehicles/maintenancetype_list.html'
    context_object_name = 'maintenance_types'
    paginate_by = 10

class MaintenanceTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'vehicles.add_maintenancetype'
    model = MaintenanceType
    template_name = 'vehicles/maintenancetype_form.html'
    fields = ['name', 'description', 'estimated_cost']
    success_url = reverse_lazy('maintenancetype_list')

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de servicio creado exitosamente')
        return super().form_valid(form)

class MaintenanceTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'vehicles.change_maintenancetype'
    model = MaintenanceType
    template_name = 'vehicles/maintenancetype_form.html'
    fields = ['name', 'description', 'estimated_cost']
    success_url = reverse_lazy('maintenancetype_list')

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de servicio actualizado exitosamente')
        return super().form_valid(form)

class MaintenanceTypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'vehicles.delete_maintenancetype'
    model = MaintenanceType
    template_name = 'vehicles/maintenancetype_confirm_delete.html'
    success_url = reverse_lazy('maintenancetype_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Tipo de servicio eliminado exitosamente')
        return super().delete(request, *args, **kwargs)


# ----------------- BULK MAINTENANCE -----------------
from django.views.generic import TemplateView
from django.shortcuts import redirect

class MaintenanceBulkCreateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = 'vehicles.add_maintenance'
    template_name = 'vehicles/maintenance_bulk_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicles'] = Vehicle.objects.all()
        context['maintenance_types'] = MaintenanceType.objects.all()
        context['workshops'] = Workshop.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        vehicle_id = request.POST.get('vehicle')
        services = request.POST.getlist('services')
        
        if not vehicle_id or not services:
            messages.error(request, 'Debes seleccionar al menos un servicio')
            return redirect('maintenance_bulk_add')
        
        vehicle = Vehicle.objects.get(id=vehicle_id)
        count = 0
        
        for service_id in services:
            maintenance_type = MaintenanceType.objects.get(id=service_id)
            detected_by = request.POST.get(f'detected_by_{service_id}', 'Sistema')
            problem_description = request.POST.get(f'problem_{service_id}', '')
            
            Maintenance.objects.create(
                vehicle=vehicle,
                maintenance_type=maintenance_type,
                status='Detectado',
                detected_by=detected_by,
                problem_description=problem_description
            )
            count += 1
        
        messages.success(request, f'{count} problema(s) detectado(s) exitosamente')
        return redirect('maintenance_list')
