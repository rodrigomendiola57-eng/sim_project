from django.db import models

class Vehicle(models.Model):
    plate = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Active','Active'), ('Maintenance','Maintenance'), ('Out of service','Out of service')])

    def __str__(self):
        return f"{self.plate} - {self.brand} {self.model}"

class Document(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=50)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.doc_type} - {self.vehicle.plate}"

class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    maintenance_type = models.CharField(max_length=50)
    date = models.DateField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.maintenance_type} - {self.vehicle.plate}"


