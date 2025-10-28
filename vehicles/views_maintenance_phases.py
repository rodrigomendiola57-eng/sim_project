from django.views.generic import DetailView, UpdateView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Maintenance
from datetime import date

class MaintenanceDetailView(DetailView):
    model = Maintenance
    template_name = 'vehicles/maintenance_detail.html'
    context_object_name = 'maintenance'

class MaintenanceQuoteView(UpdateView):
    model = Maintenance
    template_name = 'vehicles/maintenance_quote.html'
    fields = ['workshop', 'estimated_cost', 'quote_file']
    success_url = reverse_lazy('maintenance_list')
    
    def form_valid(self, form):
        form.instance.status = 'Cotizado'
        form.instance.quote_date = date.today()
        messages.success(self.request, 'Cotización agregada exitosamente')
        return super().form_valid(form)

class MaintenanceApproveView(UpdateView):
    model = Maintenance
    template_name = 'vehicles/maintenance_approve.html'
    fields = ['approved_by', 'approval_notes']
    success_url = reverse_lazy('maintenance_list')
    
    def form_valid(self, form):
        form.instance.status = 'Aprobado'
        form.instance.approval_date = date.today()
        messages.success(self.request, 'Mantenimiento aprobado exitosamente')
        return super().form_valid(form)

class MaintenanceRejectView(UpdateView):
    model = Maintenance
    template_name = 'vehicles/maintenance_reject.html'
    fields = ['approved_by', 'approval_notes']
    success_url = reverse_lazy('maintenance_list')
    
    def form_valid(self, form):
        form.instance.status = 'Rechazado'
        form.instance.approval_date = date.today()
        messages.warning(self.request, 'Mantenimiento rechazado')
        return super().form_valid(form)

class MaintenanceCompleteView(UpdateView):
    model = Maintenance
    template_name = 'vehicles/maintenance_complete.html'
    fields = ['date', 'cost', 'invoice_file', 'notes']
    success_url = reverse_lazy('maintenance_list')
    
    def form_valid(self, form):
        form.instance.status = 'Completado'
        if not form.instance.date:
            form.instance.date = date.today()
        messages.success(self.request, 'Mantenimiento completado exitosamente')
        return super().form_valid(form)
