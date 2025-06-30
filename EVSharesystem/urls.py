"""URL configuration for EVSharesystem project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.contrib import admin
from django.urls import path
from customer import views
from customer.views import login_view, register, custom_logout
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.shortcuts import redirect
from customer.views import vehicles, locations, pricing


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Logged out successfully!")
        return super().dispatch(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('login/', views.login_view, name='login'), 
    path('register/', register, name='register'),
    path('customer/dashboard/', views.customer_dashboard, name='customer_dashboard'),  # Redirects to home
    path('operator/dashboard/', views.operator_dashboard, name='operator_dashboard'),
    path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('vehicles/', vehicles, name='vehicles'),
    path('locations/', locations, name='locations'),
    path('pricing/', pricing, name='pricing'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('rent/', views.rent_vehicle, name='rent_vehicle'),
    path('return-vehicle/', views.return_vehicle, name='return_vehicle'),
    path('report-vehicle/', views.report_vehicle, name='report_vehicle'),
    path('pay-charges/', views.pay_charges, name='pay_charges'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('get_places/<str:city>/', views.get_places, name='get_places'),

    path('operator/track_vehicles/', views.track_vehicles, name='track_vehicles'),
    path('operator/charge_vehicles/', views.charge_vehicles, name='charge_vehicles'),
    path('operator/charge_vehicle/<int:vehicle_id>/', views.charge_vehicle, name='charge_vehicle'),
    path('operator/repair_vehicle/', views.repair_vehicle, name='repair_vehicle'),
    path('operator/move_vehicle/', views.move_vehicle_page, name='move_vehicle_page'),
    path('operator/move_vehicle_ajax/', views.move_vehicle_ajax, name='move_vehicle_ajax'),

    path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/daily-rentals-data/', views.get_daily_rentals_data, name='get_daily_rentals_data'),
    path('manager/payment-plan-data/', views.get_payment_plan_data, name='get_payment_plan_data'),
    path('manager/revenue-by-city-data/', views.get_revenue_by_city_data, name='get_revenue_by_city_data'),
    path('manager/vehicle-availability-status/', views.vehicle_availability_status, name='vehicle_availability_status'),

    path('manager/average-ratings-vehicle-types/', views.average_ratings_vehicle_types, name='average_ratings_vehicle_types'),
    path('manager/defective-reports-by-city/', views.defective_reports_by_city_data, name='defective_reports_by_city_data'),
    path('manager/rental-distribution/', views.rental_distribution_by_type, name='rental_distribution_by_type'),


    path('customer/feedback/', views.feedback_page, name='feedback_page'),
    path('customer/feedback/submit/<int:rental_id>/', views.submit_feedback, name='submit_feedback'),
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
    path('vip/', views.vip, name='vip'),
    path('profile/', views.profile_view, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
]

