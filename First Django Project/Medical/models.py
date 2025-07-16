from django.db import models
class Patient(models.Model):
    """Patient who orders medicine"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    
    def __str__(self):
        return self.name

class Facilities(models.Model):
    """Where medicine is to be  delivered (hospital, clinic, pharmacy)"""
    name = models.CharField(max_length=100)
    facility_type = models.CharField(max_length=20, choices=[
        ('hospital', 'Hospital'),
        ('clinic', 'Clinic'),
        ('pharmacy', 'Pharmacy'),
    ])
    address = models.TextField()
    
    def __str__(self):
        return f"{self.name} ({self.facility_type})"

class Prescription(models.Model):
    """Medicine/Drug that can be ordered"""
    medicine_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_quantity = models.IntegerField()
    
    def __str__(self):
        return self.medicine_name

class Shipment(models.Model):
    """Order from patient - delivered to facility"""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facilities, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Prescription, through='ShipmentItem')
    
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ], default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.order_number} - {self.patient.name}"

class ShipmentItem(models.Model):
    """Bridge table: Which medicines in which shipment"""
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.prescription.medicine_name} x {self.quantity}"