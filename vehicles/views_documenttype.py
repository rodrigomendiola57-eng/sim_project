from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import DocumentType

class DocumentTypeListView(ListView):
    model = DocumentType
    template_name = 'vehicles/documenttype_list.html'
    context_object_name = 'document_types'
    paginate_by = 20

class DocumentTypeCreateView(CreateView):
    model = DocumentType
    template_name = 'vehicles/documenttype_form.html'
    fields = ['name', 'description', 'validity_months', 'is_required']
    success_url = reverse_lazy('documenttype_list')

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de documento creado exitosamente')
        return super().form_valid(form)

class DocumentTypeUpdateView(UpdateView):
    model = DocumentType
    template_name = 'vehicles/documenttype_form.html'
    fields = ['name', 'description', 'validity_months', 'is_required']
    success_url = reverse_lazy('documenttype_list')

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de documento actualizado exitosamente')
        return super().form_valid(form)

class DocumentTypeDeleteView(DeleteView):
    model = DocumentType
    template_name = 'vehicles/documenttype_confirm_delete.html'
    success_url = reverse_lazy('documenttype_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Tipo de documento eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
