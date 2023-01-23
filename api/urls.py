from django.urls import path

from .views import CustomerList, CustomerDetail, VehicleTypeList, VehicleTypeDetail, VehicleList, VehicleDetail, BookingList, BookingDetail

urlpatterns = [
    path('customer/', CustomerList.as_view()),
    path('customer/<int:pk>', CustomerDetail.as_view()),
    path('vehicletype/', VehicleTypeList.as_view()),
    path('vehicletype/<int:pk>', VehicleTypeDetail.as_view()),
    path('vehicle/', VehicleList.as_view()),
    path('vehicle/<int:pk>', VehicleDetail.as_view()),
    path('booking/', BookingList.as_view()),
    path('booking/<int:pk>', BookingDetail.as_view()),
]
