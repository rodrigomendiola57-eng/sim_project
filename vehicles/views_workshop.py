from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Workshop

class WorkshopListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'vehicles.view_workshop'
    model = Workshop
    template_name = 'vehicles/workshop_list.html'
    context_object_name = 'workshops'
    paginate_by = 10

class WorkshopCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'vehicles.add_workshop'
    model = Workshop
    template_name = 'vehicles/workshop_form.html'
    fields = ['name', 'phone', 'address']
    success_url = reverse_lazy('workshop_list')

    def form_valid(self, form):
        messages.success(self.request, 'Taller creado exitosamente')
        return super().form_valid(form)

class WorkshopUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'vehicles.change_workshop'
    model = Workshop
    template_name = 'vehicles/workshop_form.html'
    fields = ['name', 'phone', 'address']
    success_url = reverse_lazy('workshop_list')

    def form_valid(self, form):
        messages.success(self.request, 'Taller actualizado exitosamente')
        return super().form_valid(form)

class WorkshopDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'vehicles.delete_workshop'
    model = Workshop
    template_name = 'vehicles/workshop_confirm_delete.html'
    success_url = reverse_lazy('workshop_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Taller eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
