from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import VehicleChecklist, Vehicle

class ChecklistListView(LoginRequiredMixin, ListView):
    model = VehicleChecklist
    template_name = 'vehicles/checklist_list.html'
    context_object_name = 'checklists'
    paginate_by = 20

class ChecklistCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'vehicles.add_vehiclechecklist'
    model = VehicleChecklist
    template_name = 'vehicles/checklist_form.html'
    fields = '__all__'
    success_url = reverse_lazy('checklist_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicles'] = Vehicle.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        VehicleChecklist.objects.create(
            vehicle_id=request.POST.get('vehicle'),
            driver_name=request.POST.get('driver_name'),
            station=request.POST.get('station'),
            tires_condition=request.POST.get('tires_condition'),
            tires_pressure=request.POST.get('tires_pressure'),
            lights=request.POST.get('lights'),
            mirrors=request.POST.get('mirrors'),
            windshield=request.POST.get('windshield'),
            wipers=request.POST.get('wipers'),
            body_damage=request.POST.get('body_damage'),
            seat_belts=request.POST.get('seat_belts'),
            horn=request.POST.get('horn'),
            dashboard_lights=request.POST.get('dashboard_lights'),
            air_conditioning=request.POST.get('air_conditioning'),
            brakes=request.POST.get('brakes'),
            engine=request.POST.get('engine'),
            oil_level=request.POST.get('oil_level'),
            coolant_level=request.POST.get('coolant_level'),
            battery=request.POST.get('battery'),
            fire_extinguisher=request.POST.get('fire_extinguisher'),
            first_aid_kit=request.POST.get('first_aid_kit'),
            warning_triangles=request.POST.get('warning_triangles'),
            observations=request.POST.get('observations', ''),
            odometer_reading=request.POST.get('odometer_reading'),
            fuel_level=request.POST.get('fuel_level'),
        )
        messages.success(request, 'Checklist guardado exitosamente')
        return redirect('checklist_list')

class ChecklistDetailView(LoginRequiredMixin, DetailView):
    model = VehicleChecklist
    template_name = 'vehicles/checklist_detail.html'
    context_object_name = 'checklist'

class ChecklistDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'vehicles.delete_vehiclechecklist'
    model = VehicleChecklist
    template_name = 'vehicles/checklist_confirm_delete.html'
    success_url = reverse_lazy('checklist_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Checklist eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
