from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Sim(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Suspendido', 'Suspendido'),
    ]
    
    OPERADOR_CHOICES = [
        ('Telcel', 'Telcel'),
        ('Movistar', 'Movistar'),
        ('AT&T', 'AT&T'),
        ('Otro', 'Otro'),
    ]
    
    numero = models.CharField(max_length=20, unique=True, verbose_name='Número')
    iccid = models.CharField(max_length=30, unique=True, verbose_name='ICCID')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Activo', verbose_name='Estado')
    operador = models.CharField(max_length=50, choices=OPERADOR_CHOICES, verbose_name='Operador')
    fecha_activacion = models.DateField(null=True, blank=True, verbose_name='Fecha de Activación')
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    
    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'SIM'
        verbose_name_plural = 'SIMs'
    
    def __str__(self):
        return f"{self.numero} - {self.operador}"

class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Maintenance', 'Maintenance'),
        ('Out of service', 'Out of service')
    ]
    
    plate = models.CharField(max_length=10, unique=True, verbose_name='Placa')
    brand = models.CharField(max_length=50, verbose_name='Marca')
    model = models.CharField(max_length=50, verbose_name='Modelo')
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year + 1)],
        verbose_name='Año'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active', verbose_name='Estado')
    station = models.CharField(max_length=100, blank=True, null=True, verbose_name='Estación')
    photo = models.ImageField(upload_to='vehicles/', null=True, blank=True, verbose_name='Foto')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
        indexes = [models.Index(fields=['plate'])]

    def __str__(self):
        return f"{self.plate} - {self.brand} {self.model}"

class DocumentType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')
    validity_months = models.IntegerField(null=True, blank=True, verbose_name='Vigencia (meses)')
    is_required = models.BooleanField(default=True, verbose_name='Obligatorio')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'
    
    def __str__(self):
        return self.name

class Document(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='documents', verbose_name='Vehículo')
    doc_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, verbose_name='Tipo de Documento')
    issue_date = models.DateField(verbose_name='Fecha de Emisión')
    expiry_date = models.DateField(verbose_name='Fecha de Vencimiento')
    document_number = models.CharField(max_length=100, blank=True, verbose_name='Número de Documento')
    document_file = models.ImageField(upload_to='vehicle_documents/', null=True, blank=True, verbose_name='Archivo')
    notes = models.TextField(blank=True, verbose_name='Notas')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-expiry_date']
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        indexes = [models.Index(fields=['expiry_date'])]

    def __str__(self):
        return f"{self.doc_type.name} - {self.vehicle.plate}"

    @property
    def is_expired(self):
        from datetime import date
        return self.expiry_date < date.today()

class Workshop(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del Taller')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    address = models.TextField(verbose_name='Dirección')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Taller'
        verbose_name_plural = 'Talleres'
    
    def __str__(self):
        return self.name

class MaintenanceType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')
    estimated_cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Costo Estimado')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Tipo de Mantenimiento'
        verbose_name_plural = 'Tipos de Mantenimiento'
    
    def __str__(self):
        return self.name

class Maintenance(models.Model):
    STATUS_CHOICES = [
        ('Detectado', 'Detectado'),
        ('Cotizado', 'Cotizado'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
        ('Completado', 'Completado'),
    ]
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenances', verbose_name='Vehículo')
    maintenance_type = models.ForeignKey(MaintenanceType, on_delete=models.PROTECT, verbose_name='Tipo de Mantenimiento')
    workshop = models.ForeignKey(Workshop, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Taller')
    
    # Fase 1: Detección
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Detectado', verbose_name='Estado')
    detection_date = models.DateField(auto_now_add=True, verbose_name='Fecha de Detección')
    detected_by = models.CharField(max_length=200, default='Sistema', verbose_name='Detectado por')
    problem_description = models.TextField(default='', verbose_name='Descripción del Problema')
    
    # Fase 2: Cotización
    quote_date = models.DateField(null=True, blank=True, verbose_name='Fecha de Cotización')
    estimated_cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)], verbose_name='Costo Cotizado')
    quote_file = models.FileField(upload_to='maintenance_quotes/', null=True, blank=True, verbose_name='Archivo de Cotización')
    
    # Fase 3: Aprobación
    approval_date = models.DateField(null=True, blank=True, verbose_name='Fecha de Aprobación')
    approved_by = models.CharField(max_length=200, blank=True, verbose_name='Aprobado por')
    approval_notes = models.TextField(blank=True, verbose_name='Notas de Aprobación')
    
    # Ejecución
    date = models.DateField(null=True, blank=True, verbose_name='Fecha de Realización')
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)], verbose_name='Costo Real')
    invoice_file = models.FileField(upload_to='maintenance_invoices/', null=True, blank=True, verbose_name='Factura')
    notes = models.TextField(blank=True, verbose_name='Notas')
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'
        indexes = [models.Index(fields=['status']), models.Index(fields=['detection_date'])]

    def __str__(self):
        return f"{self.maintenance_type.name} - {self.vehicle.plate} [{self.status}]"

class VehicleChecklist(models.Model):
    STATUS_CHOICES = [('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')]
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='checklists')
    driver_name = models.CharField(max_length=100)
    inspection_date = models.DateTimeField(auto_now_add=True)
    tires_condition = models.CharField(max_length=10, choices=STATUS_CHOICES)
    tires_pressure = models.CharField(max_length=10, choices=STATUS_CHOICES)
    lights = models.CharField(max_length=10, choices=STATUS_CHOICES)
    mirrors = models.CharField(max_length=10, choices=STATUS_CHOICES)
    windshield = models.CharField(max_length=10, choices=STATUS_CHOICES)
    wipers = models.CharField(max_length=10, choices=STATUS_CHOICES)
    body_damage = models.CharField(max_length=10, choices=STATUS_CHOICES)
    seat_belts = models.CharField(max_length=10, choices=STATUS_CHOICES)
    horn = models.CharField(max_length=10, choices=STATUS_CHOICES)
    dashboard_lights = models.CharField(max_length=10, choices=STATUS_CHOICES)
    air_conditioning = models.CharField(max_length=10, choices=STATUS_CHOICES)
    brakes = models.CharField(max_length=10, choices=STATUS_CHOICES)
    engine = models.CharField(max_length=10, choices=STATUS_CHOICES)
    oil_level = models.CharField(max_length=10, choices=STATUS_CHOICES)
    coolant_level = models.CharField(max_length=10, choices=STATUS_CHOICES)
    battery = models.CharField(max_length=10, choices=STATUS_CHOICES)
    fire_extinguisher = models.CharField(max_length=10, choices=STATUS_CHOICES)
    first_aid_kit = models.CharField(max_length=10, choices=STATUS_CHOICES)
    warning_triangles = models.CharField(max_length=10, choices=STATUS_CHOICES)
    observations = models.TextField(blank=True)
    odometer_reading = models.IntegerField()
    fuel_level = models.CharField(max_length=20, choices=[('Lleno', 'Lleno'), ('3/4', '3/4'), ('1/2', '1/2'), ('1/4', '1/4'), ('Vacío', 'Vacío')])
    
    class Meta:
        ordering = ['-inspection_date']
    
    def __str__(self):
        return f"{self.vehicle.plate} - {self.driver_name}"
    
    @property
    def overall_status(self):
        statuses = [self.tires_condition, self.tires_pressure, self.lights, self.mirrors, self.windshield, self.wipers, self.body_damage, self.seat_belts, self.horn, self.dashboard_lights, self.air_conditioning, self.brakes, self.engine, self.oil_level, self.coolant_level, self.battery, self.fire_extinguisher, self.first_aid_kit, self.warning_triangles]
        if 'Malo' in statuses:
            return 'Malo'
        elif 'Regular' in statuses:
            return 'Regular'
        return 'Bueno'

class Driver(models.Model):
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Vacaciones', 'Vacaciones'),
    ]
    
    full_name = models.CharField(max_length=200, verbose_name='Nombre Completo')
    position = models.CharField(max_length=100, default='Chofer', verbose_name='Puesto')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    email = models.EmailField(blank=True, verbose_name='Correo Electrónico')
    address = models.TextField(blank=True, verbose_name='Dirección')
    license_number = models.CharField(max_length=50, verbose_name='Número de Licencia')
    license_expiry = models.DateField(verbose_name='Vencimiento de Licencia')
    hire_date = models.DateField(verbose_name='Fecha de Contratación')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Activo', verbose_name='Estado')
    notes = models.TextField(blank=True, verbose_name='Notas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['full_name']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Lista de Empleados'
    
    def __str__(self):
        return self.full_name

class DriverDocument(models.Model):
    DOCUMENT_TYPES = [
        ('INE', 'INE / Identificación Oficial'),
        ('Licencia', 'Licencia de Conducir'),
        ('Antecedentes', 'Carta de No Antecedentes Penales'),
        ('Solicitud', 'Solicitud de Empleo'),
        ('Comprobante', 'Comprobante de Domicilio'),
        ('CURP', 'CURP'),
        ('RFC', 'RFC'),
        ('NSS', 'Número de Seguro Social'),
        ('Contrato', 'Contrato Laboral'),
        ('Otro', 'Otro Documento'),
    ]
    
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='documents', verbose_name='Empleado')
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES, verbose_name='Tipo de Documento')
    document_file = models.ImageField(upload_to='driver_documents/', verbose_name='Archivo')
    description = models.CharField(max_length=200, blank=True, verbose_name='Descripción')
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')
    
    class Meta:
        ordering = ['-upload_date']
        verbose_name = 'Documento de Empleado'
        verbose_name_plural = 'Documentos de Empleados'
    
    def __str__(self):
        return f"{self.driver.full_name} - {self.document_type}"
