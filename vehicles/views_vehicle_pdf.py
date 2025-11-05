from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate as PDFDoc, Table, TableStyle, Paragraph, Spacer, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from io import BytesIO
from datetime import datetime
from .models import Vehicle, Maintenance, Document, VehicleChecklist

class VehiclePDFView(LoginRequiredMixin, View):
    def get(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        
        # Crear PDF
        buffer = BytesIO()
        pdf_doc = PDFDoc(buffer, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
        elements = []
        styles = getSampleStyleSheet()
        
        # Estilos personalizados
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#80AD46'),
            alignment=TA_CENTER,
            spaceAfter=10,
            fontName='Helvetica-Bold'
        )
        
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#6B9239'),
            spaceAfter=10,
            fontName='Helvetica-Bold'
        )
        
        section_style = ParagraphStyle(
            'SectionTitle',
            parent=styles['Heading3'],
            fontSize=12,
            textColor=colors.HexColor('#80AD46'),
            spaceAfter=8,
            spaceBefore=15,
            fontName='Helvetica-Bold'
        )
        
        # Encabezado
        elements.append(Paragraph("FICHA GENERAL DEL VEHÍCULO", title_style))
        elements.append(Paragraph("Sistema Integral de Mantenimiento - ICASA", subtitle_style))
        elements.append(Paragraph(f"Generado: {datetime.now().strftime('%d/%m/%Y %H:%M')}", styles['Normal']))
        elements.append(Spacer(1, 20))
        
        # Información del Vehículo
        elements.append(Paragraph("INFORMACIÓN DEL VEHÍCULO", section_style))
        
        vehicle_data = [
            ['Placa:', vehicle.plate],
            ['Marca:', vehicle.brand],
            ['Modelo:', vehicle.model],
            ['Año:', str(vehicle.year)],
            ['Estado:', vehicle.status],
            ['Estación:', vehicle.station or 'N/A'],
            ['Fecha de Registro:', vehicle.created_at.strftime('%d/%m/%Y') if vehicle.created_at else 'N/A']
        ]
        
        vehicle_table = Table(vehicle_data, colWidths=[2*inch, 4*inch])
        vehicle_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F0FDF4')),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#6B9239')),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ]))
        elements.append(vehicle_table)
        elements.append(Spacer(1, 20))
        
        # Documentos
        documents = Document.objects.filter(vehicle=vehicle).select_related('doc_type')
        if documents.exists():
            elements.append(Paragraph("DOCUMENTOS", section_style))
            
            doc_data = [['Tipo', 'Número', 'Emisión', 'Vencimiento', 'Estado']]
            for doc in documents:
                estado = 'Vencido' if doc.is_expired else 'Vigente'
                doc_data.append([
                    doc.doc_type.name,
                    doc.document_number or '-',
                    doc.issue_date.strftime('%d/%m/%Y'),
                    doc.expiry_date.strftime('%d/%m/%Y'),
                    estado
                ])
            
            doc_table = Table(doc_data, colWidths=[1.8*inch, 1.2*inch, 1*inch, 1*inch, 1*inch])
            doc_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#80AD46')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 9),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9FAFB')]),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            elements.append(doc_table)
            elements.append(Spacer(1, 20))
        
        # Mantenimientos
        maintenances = Maintenance.objects.filter(vehicle=vehicle).select_related('maintenance_type', 'workshop').order_by('-created_at')[:15]
        if maintenances.exists():
            elements.append(Paragraph("HISTORIAL DE MANTENIMIENTOS (Últimos 15)", section_style))
            
            maint_data = [['Fecha', 'Tipo', 'Estado', 'Taller', 'Costo']]
            for maint in maintenances:
                costo = f"${maint.cost}" if maint.cost else (f"~${maint.estimated_cost}" if maint.estimated_cost else '-')
                maint_data.append([
                    maint.detection_date.strftime('%d/%m/%Y'),
                    maint.maintenance_type.name[:30],
                    maint.status,
                    maint.workshop.name[:25] if maint.workshop else '-',
                    costo
                ])
            
            maint_table = Table(maint_data, colWidths=[1*inch, 2*inch, 1.2*inch, 1.5*inch, 0.8*inch])
            maint_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#80AD46')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9FAFB')]),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ]))
            elements.append(maint_table)
            elements.append(Spacer(1, 20))
        
        # Checklists
        checklists = VehicleChecklist.objects.filter(vehicle=vehicle).order_by('-inspection_date')[:10]
        if checklists.exists():
            elements.append(Paragraph("CHECKLISTS DE INSPECCIÓN (Últimos 10)", section_style))
            
            check_data = [['Fecha', 'Conductor', 'Estación', 'Estado', 'Odómetro']]
            for check in checklists:
                check_data.append([
                    check.inspection_date.strftime('%d/%m/%Y %H:%M'),
                    check.driver_name[:25],
                    check.station or '-',
                    check.overall_status,
                    f"{check.odometer_reading} km"
                ])
            
            check_table = Table(check_data, colWidths=[1.3*inch, 1.8*inch, 1.3*inch, 0.9*inch, 1.2*inch])
            check_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#80AD46')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9FAFB')]),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ]))
            elements.append(check_table)
            elements.append(Spacer(1, 20))
        
        # Resumen de Costos
        total_cost = sum([m.cost for m in maintenances if m.cost])
        if total_cost > 0:
            elements.append(Paragraph("RESUMEN DE COSTOS", section_style))
            
            cost_data = [
                ['Total en Mantenimientos:', f"${total_cost:,.2f}"],
                ['Cantidad de Mantenimientos:', str(maintenances.count())],
                ['Promedio por Mantenimiento:', f"${total_cost/maintenances.count():,.2f}" if maintenances.count() > 0 else '$0.00']
            ]
            
            cost_table = Table(cost_data, colWidths=[3*inch, 2*inch])
            cost_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F0FDF4')),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#6B9239')),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('LEFTPADDING', (0, 0), (-1, -1), 10),
                ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ]))
            elements.append(cost_table)
        
        # Pie de página
        elements.append(Spacer(1, 30))
        footer_style = ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=8,
            textColor=colors.grey,
            alignment=TA_CENTER
        )
        elements.append(Paragraph("ICASA - Integradores de Carga Aérea", footer_style))
        elements.append(Paragraph("Sistema Integral de Mantenimiento (SIM)", footer_style))
        
        # Construir PDF
        pdf_doc.build(elements)
        buffer.seek(0)
        
        # Respuesta
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=Ficha_{vehicle.plate}_{datetime.now().strftime("%Y%m%d")}.pdf'
        return response
