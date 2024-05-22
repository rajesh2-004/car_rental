from django.contrib import admin
from .models import CarCategory, Location, Car, Customer, Rental

@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'country', 'zip_code')
    search_fields = ('name', 'city', 'state', 'country')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('category', 'model', 'year', 'color', 'mileage', 'location', 'available')
    list_filter = ('available', 'location', 'year', 'category')
    search_fields = ('model',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'date_of_birth')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('customer', 'car', 'rental_date', 'return_date', 'daily_rate', 'total_amount')
    list_filter = ('rental_date', 'return_date', 'car')
    search_fields = ('customer__user__username', 'car__model')
