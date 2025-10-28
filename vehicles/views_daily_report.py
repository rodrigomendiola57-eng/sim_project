from django.views import View
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from datetime import date, timedelta
from .models import Document, Maintenance, VehicleChecklist

class DailyReportPDFView(View):
    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="reporte_diario_{date.today()}.pdf"'
        
        doc = SimpleDocTemplate(response, pagesize=letter)
        elements = []
        styles = getSampleStyleSheet()
        
        # Título
        title = Paragraph(f"<b>REPORTE DIARIO DE ACTIVIDADES</b><br/>{date.today().strftime('%d/%m/%Y')}", styles['Title'])
        elements.append(title)
        elements.append(Spacer(1, 20))
        
        # Documentos Vencidos
        expired_docs = Document.objects.filter(expiry_date__lt=date.today()).select_related('vehicle', 'doc_type')
        elements.append(Paragraph("<b>DOCUMENTOS VENCIDOS</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))
        
        if expired_docs:
            data = [['Vehículo', 'Tipo Documento', 'Fecha Vencimiento', 'Días Vencido']]
            for doc in expired_docs:
                days_expired = (date.today() - doc.expiry_date).days
                data.append([
                    doc.vehicle.plate,
                    doc.doc_type.name,
                    doc.expiry_date.strftime('%d/%m/%Y'),
                    f'{days_expired} días'
                ])
            
            table = Table(data, colWidths=[100, 150, 120, 100])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.red),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(table)
        else:
            elements.append(Paragraph("No hay documentos vencidos", styles['Normal']))
        
        elements.append(Spacer(1, 20))
        
        # Documentos por Vencer (próximos 30 días)
        expiring_docs = Document.objects.filter(
            expiry_date__gte=date.today(),
            expiry_date__lte=date.today() + timedelta(days=30)
        ).select_related('vehicle', 'doc_type')
        
        elements.append(Paragraph("<b>DOCUMENTOS POR VENCER (30 DÍAS)</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))
        
        if expiring_docs:
            data = [['Vehículo', 'Tipo Documento', 'Fecha Vencimiento', 'Días Restantes']]
            for doc in expiring_docs:
                days_left = (doc.expiry_date - date.today()).days
                data.append([
                    doc.vehicle.plate,
                    doc.doc_type.name,
                    doc.expiry_date.strftime('%d/%m/%Y'),
                    f'{days_left} días'
                ])
            
            table = Table(data, colWidths=[100, 150, 120, 100])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(table)
        else:
            elements.append(Paragraph("No hay documentos por vencer en los próximos 30 días", styles['Normal']))
        
        elements.append(Spacer(1, 20))
        
        # Mantenimientos del Día
        today_maintenance = Maintenance.objects.filter(date=date.today()).select_related('vehicle', 'maintenance_type')
        elements.append(Paragraph("<b>MANTENIMIENTOS DEL DÍA</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))
        
        if today_maintenance:
            data = [['Vehículo', 'Tipo Mantenimiento', 'Costo', 'Notas']]
            total_cost = 0
            for maint in today_maintenance:
                data.append([
                    maint.vehicle.plate,
                    maint.maintenance_type.name,
                    f'${maint.cost:,.2f}',
                    maint.notes[:30] if maint.notes else '-'
                ])
                total_cost += maint.cost
            
            data.append(['', 'TOTAL', f'${total_cost:,.2f}', ''])
            
            table = Table(data, colWidths=[100, 150, 100, 120])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
                ('BACKGROUND', (0, -1), (-1, -1), colors.lightblue),
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(table)
        else:
            elements.append(Paragraph("No hay mantenimientos programados para hoy", styles['Normal']))
        
        elements.append(Spacer(1, 20))
        
        # Checklists del Día
        today_checklists = VehicleChecklist.objects.filter(
            inspection_date__date=date.today()
        ).select_related('vehicle')
        
        elements.append(Paragraph("<b>CHECKLISTS DEL DÍA</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))
        
        if today_checklists:
            data = [['Vehículo', 'Conductor', 'Estado General', 'Hora']]
            for checklist in today_checklists:
                data.append([
                    checklist.vehicle.plate,
                    checklist.driver_name,
                    checklist.overall_status,
                    checklist.inspection_date.strftime('%H:%M')
                ])
            
            table = Table(data, colWidths=[100, 150, 100, 120])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.green),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(table)
        else:
            elements.append(Paragraph("No hay checklists realizados hoy", styles['Normal']))
        
        doc.build(elements)
        return response
