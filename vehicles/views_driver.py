from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from .models import Driver, DriverDocument

class DriverListView(ListView):
    model = Driver
    template_name = 'vehicles/driver_list.html'
    context_object_name = 'drivers'
    paginate_by = 20

class DriverCreateView(CreateView):
    model = Driver
    template_name = 'vehicles/driver_form.html'
    fields = ['full_name', 'position', 'phone', 'email', 'address', 'license_number', 'license_expiry', 'hire_date', 'status', 'notes']
    success_url = reverse_lazy('driver_list')

    def form_valid(self, form):
        messages.success(self.request, 'Chofer agregado exitosamente')
        return super().form_valid(form)

class DriverUpdateView(UpdateView):
    model = Driver
    template_name = 'vehicles/driver_form.html'
    fields = ['full_name', 'position', 'phone', 'email', 'address', 'license_number', 'license_expiry', 'hire_date', 'status', 'notes']
    success_url = reverse_lazy('driver_list')

    def form_valid(self, form):
        messages.success(self.request, 'Chofer actualizado exitosamente')
        return super().form_valid(form)

class DriverDetailView(DetailView):
    model = Driver
    template_name = 'vehicles/driver_detail.html'
    context_object_name = 'driver'

class DriverDeleteView(DeleteView):
    model = Driver
    template_name = 'vehicles/driver_confirm_delete.html'
    success_url = reverse_lazy('driver_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Chofer eliminado exitosamente')
        return super().delete(request, *args, **kwargs)

class DriverDocumentUploadView(View):
    def post(self, request, pk):
        driver = get_object_or_404(Driver, pk=pk)
        DriverDocument.objects.create(
            driver=driver,
            document_type=request.POST.get('document_type'),
            document_file=request.FILES.get('document_file'),
            description=request.POST.get('description', '')
        )
        messages.success(request, 'Documento subido exitosamente')
        return redirect('driver_detail', pk=pk)

class DriverDocumentDeleteView(DeleteView):
    model = DriverDocument
    
    def get_success_url(self):
        return reverse_lazy('driver_detail', kwargs={'pk': self.object.driver.pk})
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Documento eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
