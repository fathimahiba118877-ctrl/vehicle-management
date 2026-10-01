from django.db import models
from django.utils import timezone


class ServiceRequest(models.Model):
    VEHICLE_CHOICES = [
        ('Car', 'Car'),
        ('Bike', 'Bike'),
        ('SUV', 'SUV'),
        ('Van', 'Van'),
    ]

    SERVICE_CHOICES = [
        ('General Service', 'General Service'),
        ('Oil Change', 'Oil Change'),
        ('Brake Service', 'Brake Service'),
        ('Engine Service', 'Engine Service'),
        ('AC Service', 'AC Service'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=255)
    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    service_date = models.DateField()
    description = models.TextField()
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.customer_name} - {self.vehicle_number}"