from datetime import datetime, timedelta

from django.utils.dateparse import parse_datetime
from rest_framework.test import APIClient, APITestCase
from rest_framework import serializers, status

from base.models import Customer, VehicleType, Vehicle, Booking


class CustomerTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.data = {
            'firstName': 'TestFirstName',
            'lastName': 'TestLastName'
        }
        self.url = '/api/customer/'

    def testListCustomer(self):
        self.customer = Customer.objects.create(
            lastName='TestLastName', firstName='TestFirstName')

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(list(response.data)), 1)
        self.assertEqual(response.data[0]['firstName'], 'TestFirstName')
        self.assertEqual(response.data[0]['lastName'], 'TestLastName')

    def testListCustomerWithFilter(self):
        self.customer = Customer.objects.create(
            lastName='TestLastName', firstName='TestFirstName')

        response = self.client.get(
            self.url, {'lastname': 'TestLastName'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(list(response.data)), 1)
        self.assertEqual(response.data[0]['firstName'], 'TestFirstName')
        self.assertEqual(response.data[0]['lastName'], 'TestLastName')

    def testListCustomerWithFilterNoMatching(self):
        self.customer = Customer.objects.create(
            lastName='TestLastName', firstName='TestFirstName')

        response = self.client.get(
            self.url, {'lastname': 'Test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(list(response.data)), 0)

    def testCreateCustomer(self):
        data = self.data
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(response.data['firstName'], data['firstName'])
        self.assertEqual(response.data['lastName'], data['lastName'])

    def testCreateCustomerWithoutFirstName(self):
        data = self.data
        data.pop('firstName')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateCustomerWithBlankFirstName(self):
        data = self.data
        data['firstName'] = ''
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateCustomerWithoutLastName(self):
        data = self.data
        data.pop('lastName')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateCustomerWithBlankLastName(self):
        data = self.data
        data['lastName'] = ''
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class VehicleTypeTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.data = {
            'name': 'TestVehicleType'
        }
        self.url = '/api/vehicletype/'

    def testCreateVehicleType(self):
        data = self.data
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VehicleType.objects.count(), 1)
        self.assertEqual(response.data['name'], data['name'])

    def testCreateVehicleTypeWithoutName(self):
        data = {}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateVehicleTypeWithBlankName(self):
        data = {
            'name': ''
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class VehicleTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        VehicleType.objects.create(name='TestVehicleType')
        self.data = {
            'name': 'TestVehicle',
            'type': 1
        }
        self.url = '/api/vehicle/'

    def testCreateVehicle(self):
        data = self.data
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vehicle.objects.count(), 1)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['type'], data['type'])

    def testCreateVehicleWithoutName(self):
        data = self.data
        data.pop('name')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateVehicleWithBlankName(self):
        data = self.data
        data = {
            'name': ''
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateVehicleWithoutType(self):
        data = self.data
        data.pop('type')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateVehicleWithBlankType(self):
        data = {
            'type': ''
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class BookingTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.vehicleType = VehicleType.objects.create(name='TestVehicleType')
        self.vehicle = Vehicle.objects.create(
            name='TestVehicle', type=self.vehicleType)
        self.customer = Customer.objects.create(lastName='TestLastName',
                                                firstName='TestFirstName')
        self.now = datetime.now()
        self.data = {
            'customer': 1,
            'vehicle': 1,
            'start_time': self.now,
            'end_time': self.now + timedelta(days=1)
        }
        self.url = '/api/booking/'

    def testCreateBooking(self):
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(response.data['customer'], data['customer'])
        self.assertEqual(response.data['vehicle'], data['vehicle'])
        self.assertEqual(parse_datetime(
            response.data['start_time']).timestamp(), data['start_time'].timestamp())
        self.assertEqual(parse_datetime(
            response.data['end_time']).timestamp(), data['end_time'].timestamp())

    def testCreateBookingWithoutCustomer(self):
        data = self.data
        data.pop('customer')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateBookingWithBlankCustomer(self):
        data = self.data
        data = {
            'customer': ''
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateBookingWithoutVehicle(self):
        data = self.data
        data.pop('vehicle')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateBookingWithBlankVehicle(self):
        data = self.data
        data = {
            'vehicle': ''
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateBookingWithoutStartTime(self):
        data = self.data
        data.pop('start_time')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateBookingWithBlankStartTime(self):
        data = self.data
        data = {
            'start_time': ''
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateBookingWithoutEndTime(self):
        data = self.data
        data.pop('end_time')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateBookingWithBlankEndTime(self):
        data = self.data
        data = {
            'end_time': ''
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def testCreateBookingWithEndTimeBeforeStartTime(self):
        data = self.data
        data = {
            'end_time': self.now - timedelta(days=1)
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaisesMessage(
            serializers.ValidationError, 'End time must be after start time')

    def testCreateBookingWithAlreadyBookedVehicle(self):

        Booking.objects.create(customer=self.customer, vehicle=self.vehicle,
                               start_time=self.now - timedelta(hours=1), end_time=self.now + timedelta(days=1))
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaisesMessage(
            serializers.ValidationError, 'Vehicle already booked in this period')
