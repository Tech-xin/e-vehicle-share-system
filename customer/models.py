from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from datetime import time

class CustomerManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, mobile_number, age, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            age=age,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, mobile_number, age, password=None):
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_number=mobile_number,
            age=age,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Customer(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    mobile_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomerManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'mobile_number', 'age']

    def __str__(self):
        return self.username
    
class Operator(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)  # Use a hash for real applications

    def __str__(self):
        return self.username

class Manager(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)  # Use a hash for real applications

    def __str__(self):
        return self.username

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('scooter', 'E-Scooter'),
        ('bike', 'E-Bike'),
    ]
    vehicle_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES)
    city_name = models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    price_per_minute = models.DecimalField(max_digits=5, decimal_places=2)
    day_pass = models.DecimalField(max_digits=5, decimal_places=2, default=7.99)
    monthly_subscription = models.DecimalField(max_digits=5, decimal_places=2, default=28.99)
    annual_subscription = models.DecimalField(max_digits=6, decimal_places=2, default=149.99)
    opening_time = models.TimeField(default=time(8, 0), null=True, blank=True)  # Default to 8:00 AM
    closing_time = models.TimeField(default=time(22, 0), null=True, blank=True)

    is_available = models.BooleanField(default=1)  # Indicates availability
    location_lati = models.FloatField(default=55.86)  # Default latitude, e.g., Glasgow
    location_longi = models.FloatField(default=-4.25)  # Default longitude, e.g., Glasgow

    battery_level = models.DecimalField(max_digits=5, decimal_places=2, default=100.0)  # Battery level as a percentage

    def __str__(self):
        return f"{self.type} in {self.place_name}, {self.city_name}"

class Rental(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)  # Start time of rental
    end_time = models.DateTimeField(null=True, blank=True)  # End time of rental, if returned
    city_name = models.CharField(max_length=100)  # City where the rental occurred
    rented_at = models.CharField(max_length=100)  # Replacing place_name_rented
    returned_at = models.CharField(max_length=100, null=True, blank=True)
    payment_plan = models.CharField(max_length=50)  # Payment plan chosen by the customer
    is_active = models.BooleanField(default=True)  # Indicates if the rental is active
    status = models.CharField(max_length=10, default='rented')  # Tracks whether the vehicle is rented or returned

    def __str__(self): 
        return f"Rental by {self.customer.username} for {self.vehicle}"
    
class DefectiveVehicleReport(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    report_reason = models.TextField(max_length=500)
    reported_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default='Reported')  # New field
    repaired_at = models.DateTimeField(null=True, blank=True)     # New field

    def __str__(self):
        return f"Report for Vehicle {self.vehicle.vehicle_id} - Status: {self.status}"

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    payment_plan = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        vehicle_id = getattr(self.vehicle, 'id', 'N/A')
        return f"Payment by {self.customer.username} for Vehicle ID {vehicle_id} - {self.total_amount} GBP"
    
class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Link to the customer
    rental = models.ForeignKey('Rental', on_delete=models.CASCADE)  # Link to the Rental model
    vehicle_rating = models.IntegerField()  # Rating for the vehicle (1-5)
    journey_rating = models.IntegerField()  # Rating for the journey (1-5)
    experience_rating = models.IntegerField()  # Rating for overall experience (1-5)
    comments = models.TextField(blank=True, null=True)  # Optional comments
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically set date/time on submission

    class Meta:
        unique_together = ('customer', 'rental')  # Prevent duplicate feedback by same customer for the same rental

    def __str__(self):
        return f"Feedback by {self.customer} for Rental {self.rental}"
