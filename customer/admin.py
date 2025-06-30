from django.contrib import admin
from .models import Customer, Vehicle, Rental, DefectiveVehicleReport, Payment, Operator, Manager, Feedback

class CustomerAdmin(admin.ModelAdmin):
    # Defines which fields to display in the admin list view (table format)
    list_display = ('username', 'email', 'first_name', 'last_name', 'mobile_number', 'age', 'is_active', 'is_admin')

    # Adds a search bar in the admin, allowing you to search by these fields
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Adds a filter sidebar in the admin for easy filtering by 'is_active' and 'is_admin' fields
    list_filter = ('is_active', 'is_admin')

    # Defines which fields can be edited directly from the list view
    list_editable = ('is_active',)

# Register the Customer model with custom admin options
admin.site.register(Customer, CustomerAdmin)

class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle_id', 'type', 'city_name', 'place_name', 'price_per_minute', 'day_pass', 
        'monthly_subscription', 'annual_subscription', 'opening_time', 'closing_time',
        'is_available', 'location_lati', 'location_longi', 'battery_level'
    )
    search_fields = ('type', 'city_name', 'place_name', 'vehicle_id')  # Allows search by type, city, place, and ID
    list_filter = ('type', 'city_name', 'is_available')  # Adds filtering options by type, city, and availability

admin.site.register(Vehicle, VehicleAdmin)

class RentalAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id','customer', 'vehicle', 'city_name', 'rented_at', 'returned_at', 'start_time', 'end_time', 'is_active', 'status')
    list_filter = ('is_active', 'city_name', 'vehicle__type')
    search_fields = ('customer__username', 'vehicle_id', 'city_name', 'place_name_rented', 'place_name_returned')

admin.site.register(Rental, RentalAdmin)

class DefectiveVehicleReportAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id','vehicle', 'customer', 'report_reason', 'reported_at', 'status', 'repaired_at')
    list_filter = ('status', 'reported_at')
    search_fields = ('customer__username', 'vehicle_id', 'report_reason')

admin.site.register(DefectiveVehicleReport, DefectiveVehicleReportAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'vehicle', 'payment_plan', 'total_amount', 'payment_time')
    list_filter = ('payment_plan', 'payment_time')
    search_fields = ('customer__username', 'vehicle__id')

admin.site.register(Payment, PaymentAdmin)

class OperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'username', 'password')  # Display all fields in table format

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'username', 'password')  # Display all fields in table format

# Register the models with their custom admin classes
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Manager, ManagerAdmin)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer', 'rental', 'vehicle_rating', 'journey_rating', 'experience_rating', 'submitted_at')
    list_filter = ('submitted_at', 'vehicle_rating', 'journey_rating', 'experience_rating')
    search_fields = ('customer__username', 'rental__id', 'comments')
    ordering = ('-submitted_at',)