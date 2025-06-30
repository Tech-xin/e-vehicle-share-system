**Project Overview**
The E-Vehicle Share System is a web-based application that supports an electric vehicle sharing program. It allows customers to rent and return vehicles, submit feedback, and make payments. Operators can manage vehicle maintenance and track vehicle locations, while managers can generate and view analytical reports.

**Technology Stack**
1. Frontend: HTML, CSS, Bootstrap and JSON for responsive design.
2. Backend: Python, Django framework.
3. Database: SQLite.
4. Tools: Visual Studio Code, Google Maps API for tracking.

_**How to Run the Project**_
To run the E-Vehicle Share System, follow these steps:

1. Prerequisites
Ensure that you have the following installed:
A. Python 3.x
B. Django
C. SQLite

2. Download the project folder onto your device.
3. Navigate to the sub-folder that contains the manage.py file using 'cd'.
4. Run the server: `python manage.py runserver`
5. Access the project : Open your web browser and go to http://127.0.0.1:8000/ to access the application.

**Operator and Manager Login Setup:**
To create login credentials for the Operator and Manager accounts, run the following commands in the terminal:

`python manage.py shell`

`from customer.models import Operator`

`Operator.objects.create(username='operator1', name='John', surname='Doe', email='operator1@example.com', password='securepassword')`

`from customer.models import Manager`

`Manager.objects.create(username='manager1', name='Jane', surname='Smith', email='manager1@example.com', password='securepassword')`

`exit()`



**Login Credentials for Testing**
For testing purposes, the following universal credentials can be used to log in as a Customer, Operator, or Manager:

Username: Admin3
Password: Adminuser@3

_However, it is recommended to create a login separately._


**The E-Vehicle Share System includes the following key functionalities:**

1. Customer Features: Rent, return, report and pay for vehicles. 
2. Operator Features: Track Vehicles, Update vehicle status, battery levels, and availability. Move vehicles to different locations in city.
3. Manager: Create detailed reports of vehicle activities over specified time periods.

