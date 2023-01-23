Using Python and Django REST Framework, create an application which fits with this description

YourMove operates a free-floating private fleet of different sorts of vehicles: cars, bikes, motor
scooters and kick scooters. Using a mobile application, a customer can book a vehicle. They
choose a starting date and time, and a duration in order to make a reservation.
Create the data model to represent a user, a vehicle, a booking. Fields don’t matter that much,
we just need to illustrate the concept. Keep it simple.
Design a REST API with the following operations:
● Create a user
● Create a booking
● Retrieve a specific booking
● Cancel a booking
● Delete a vehicle

Make sure a vehicle cannot be booked more than once at any given time
We store the user address, and we want to geocode it
Run the app in Docker

This is a demo application. It will serve as a playground to discuss tech-to-tech during the next
interview. We don’t expect every edge case to be covered, you can identify them with TODO
comments. Take a chance to demonstrate your clean code skills and how you would build a
production ready application.

Instructions

● Use Python
● Use a web framework, hint: we use Django and FastAPI.
● We should be able to easily run your application on our computer.
● Ignore all authentication concerns, but check the framework’s documentation: how
would you protect your endpoints, with different roles (user, admin)?
● Upload your code to a Github repository and grant us access
● Do not squash all your commits, nor push a single commit at the end. We will be looking
at the history.