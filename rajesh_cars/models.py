from django.db import models
from django.contrib.auth.models import User

# Car Category Model
class CarCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Location Model
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"

# Car Model
class Car(models.Model):
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    mileage = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.model} ({self.year})"

# Customer Model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

# Rental Model
class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.return_date:
            duration = (self.return_date - self.rental_date).days
            self.total_amount = self.daily_rate * duration
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Rental {self.id} - {self.car} by {self.customer}"
