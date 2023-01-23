from rest_framework import serializers, status

from base.models import Customer, VehicleType, Vehicle, Booking


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('__all__')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('__all__')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('__all__')

    def validate(self, data):
        if data['end_time'] <= data['start_time']:
            raise serializers.ValidationError(
                "End time must be after start time", status.HTTP_400_BAD_REQUEST)
        bookingsForVehicle = Booking.objects.filter(vehicle=data['vehicle'])
        for booking in bookingsForVehicle:
            if ((booking.end_time >= data['start_time'] and booking.end_time <= data['end_time'])
                or (booking.start_time >= data['start_time'] and booking.start_time <= data['end_time'])
                or (booking.start_time <= data['start_time'] and booking.end_time >= data['end_time'])
                ):
                raise serializers.ValidationError(
                    "Vehicle already booked in this period", status.HTTP_400_BAD_REQUEST)
        return super().validate(data)
