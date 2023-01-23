from rest_framework import generics

from base.models import Customer, VehicleType, Vehicle, Booking
from .serializers import CustomerSerializer, VehicleTypeSerializer, VehicleSerializer, BookingSerializer


class CustomerList(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        customerName = self.request.query_params.get('lastname')
        if customerName is not None:
            queryset = queryset.filter(lastName=customerName)
        return queryset


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class VehicleTypeList(generics.ListCreateAPIView):
    serializer_class = VehicleTypeSerializer
    queryset = VehicleType.objects.all()


class VehicleTypeDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = VehicleTypeSerializer
    queryset = VehicleType.objects.all()


class VehicleList(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        vehicleType = self.request.query_params.get('type')
        if vehicleType is not None:
            queryset = queryset.filter(type=vehicleType)
        return queryset


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.all()
        bookingCanceled = self.request.query_params.get('canceled')
        if bookingCanceled is not None:
            queryset = queryset.filter(canceled=bookingCanceled)
        return queryset


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
