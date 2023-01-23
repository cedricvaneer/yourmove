from django.db import models

# Create your models here.


class Customer(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"


class VehicleType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Vehicle(models.Model):
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    canceled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.customer} - {self.vehicle} : {self.start_time} - {self.end_time}"
