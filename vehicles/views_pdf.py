from django.http import HttpResponse
from django.views import View
from datetime import date
from calendar import monthrange
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from .models import Maintenance

class MaintenancePDFView(View):
    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mantenimientos_mes.pdf"'
        
        today = date.today()
        first_day = today.replace(day=1)
        last_day = today.replace(day=monthrange(today.year, today.month)[1])
        
        # Obtener mantenimientos del mes (por fecha de detección)
        maintenances = Maintenance.objects.filter(
            detection_date__gte=first_day,
            detection_date__lte=last_day
        ).select_related('vehicle', 'maintenance_type', 'workshop').order_by('detection_date')
        
        # Crear PDF en orientación horizontal para más espacio
        doc = SimpleDocTemplate(response, pagesize=landscape(letter))
        elements = []
        styles = getSampleStyleSheet()
        
        # Título
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#1e3a8a'),
            spaceAfter=30,
            alignment=TA_CENTER
        )
        title = Paragraph(f"Reporte de Mantenimientos - {today.strftime('%B %Y')}", title_style)
        elements.append(title)
        
        # Información general
        info_style = ParagraphStyle('Info', parent=styles['Normal'], fontSize=10, spaceAfter=20)
        info = Paragraph(f"Fecha de generación: {today.strftime('%d/%m/%Y')}<br/>Total de mantenimientos: {maintenances.count()}", info_style)
        elements.append(info)
        elements.append(Spacer(1, 0.2*inch))
        
        # Tabla de mantenimientos
        data = [['Fecha', 'Vehículo', 'Servicio', 'Taller', 'Costo', 'Estado']]
        
        total_cost = 0
        for maint in maintenances:
            # Determinar estado en español
            if maint.status == 'Detectado':
                status_text = 'Pend. Cotiz.'
            elif maint.status == 'Cotizado':
                status_text = 'Cotizado'
            elif maint.status == 'Aprobado':
                status_text = 'Aprobado'
            elif maint.status == 'Rechazado':
                status_text = 'Rechazado'
            elif maint.status == 'Completado':
                status_text = 'Completado'
            else:
                status_text = maint.status
            
            cost_display = f'${maint.estimated_cost}' if maint.estimated_cost else '-'
            if maint.estimated_cost:
                total_cost += maint.estimated_cost
            
            data.append([
                maint.detection_date.strftime('%d/%m/%Y'),
                maint.vehicle.plate,
                maint.maintenance_type.name[:30],
                maint.workshop.name[:25] if maint.workshop else '-',
                cost_display,
                status_text
            ])
        
        # Agregar total
        data.append(['', '', '', 'TOTAL', f'${total_cost}', ''])
        
        # Crear tabla con anchos ajustados para orientación horizontal
        table = Table(data, colWidths=[1.2*inch, 1*inch, 2.5*inch, 2*inch, 1.2*inch, 1.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e3a8a')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 1), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
            ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
            ('GRID', (0, 0), (-1, -2), 1, colors.black),
            ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#e2e8f0')),
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
            ('WORDWRAP', (0, 0), (-1, -1), True),
        ]))
        
        elements.append(table)
        
        # Construir PDF
        doc.build(elements)
        return response
