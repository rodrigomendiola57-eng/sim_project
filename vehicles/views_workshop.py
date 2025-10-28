from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Workshop

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'vehicles/workshop_list.html'
    context_object_name = 'workshops'
    paginate_by = 10

class WorkshopCreateView(CreateView):
    model = Workshop
    template_name = 'vehicles/workshop_form.html'
    fields = ['name', 'phone', 'address']
    success_url = reverse_lazy('workshop_list')

    def form_valid(self, form):
        messages.success(self.request, 'Taller creado exitosamente')
        return super().form_valid(form)

class WorkshopUpdateView(UpdateView):
    model = Workshop
    template_name = 'vehicles/workshop_form.html'
    fields = ['name', 'phone', 'address']
    success_url = reverse_lazy('workshop_list')

    def form_valid(self, form):
        messages.success(self.request, 'Taller actualizado exitosamente')
        return super().form_valid(form)

class WorkshopDeleteView(DeleteView):
    model = Workshop
    template_name = 'vehicles/workshop_confirm_delete.html'
    success_url = reverse_lazy('workshop_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Taller eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
