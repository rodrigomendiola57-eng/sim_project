from django.views.generic import TemplateView
from django.db.models import Count, Q, Sum
from datetime import date, timedelta, datetime
from calendar import monthrange
from .models import Vehicle, Document, Maintenance, VehicleChecklist

class DashboardView(TemplateView):
    template_name = 'vehicles/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        thirty_days = today + timedelta(days=30)
        
        # Primer y último día del mes actual
        first_day_month = today.replace(day=1)
        last_day_month = today.replace(day=monthrange(today.year, today.month)[1])

        # Documentos vencidos
        expired_docs = Document.objects.filter(expiry_date__lt=today).select_related('vehicle')
        for doc in expired_docs:
            doc.days_expired = (today - doc.expiry_date).days

        # Documentos por vencer en 30 días
        expiring_soon_docs = Document.objects.filter(
            expiry_date__gte=today,
            expiry_date__lte=thirty_days
        ).select_related('vehicle')
        for doc in expiring_soon_docs:
            doc.days_remaining = (doc.expiry_date - today).days

        # Todos los documentos para el calendario
        all_docs = Document.objects.select_related('vehicle').all()
        for doc in all_docs:
            if doc.expiry_date < today:
                doc.days_expired = (today - doc.expiry_date).days
            else:
                doc.days_remaining = (doc.expiry_date - today).days

        # Mantenimientos del mes actual
        month_maintenances = Maintenance.objects.filter(
            date__gte=first_day_month,
            date__lte=last_day_month
        ).select_related('vehicle', 'maintenance_type').order_by('date')
        
        # Calcular días restantes para cada mantenimiento
        for maint in month_maintenances:
            maint.days_until = (maint.date - today).days
            maint.is_past = maint.date < today
        
        # Total de costos del mes
        month_total_cost = month_maintenances.aggregate(total=Sum('cost'))['total'] or 0
        
        # Checklists del día - obtener todos los de hoy
        from django.utils import timezone
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = timezone.now().replace(hour=23, minute=59, second=59, microsecond=999999)
        today_checklists = VehicleChecklist.objects.filter(
            inspection_date__gte=today_start,
            inspection_date__lte=today_end
        ).select_related('vehicle').order_by('-inspection_date')

        # Estadísticas
        context['today_checklists'] = today_checklists
        context['expired_docs'] = expired_docs
        context['expiring_soon_docs'] = expiring_soon_docs
        context['all_docs'] = all_docs
        context['month_maintenances'] = month_maintenances
        context['month_total_cost'] = month_total_cost
        context['current_month'] = today.strftime('%B %Y')
        context['total_vehicles'] = Vehicle.objects.count()
        context['active_vehicles'] = Vehicle.objects.filter(status='Active').count()
        context['maintenance_vehicles'] = Vehicle.objects.filter(status='Maintenance').count()
        context['total_documents'] = Document.objects.count()

        return context
