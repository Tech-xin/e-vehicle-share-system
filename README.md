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
   
Jessica's Contribution Description:

1. Issue Resolution and Feature Development:
   - Tackled the issue where pop-up windows could not disappear, ensuring smooth user interactions.
   - Created the move_vehicle.html page and added a left sidebar similar to Google Maps. At the same time, I implemented a form to move vehicles, which includes:
     - Added the guest's GPS location on the map with a red marker.
     - Implemented the "borrow a car nearby, return it on-site" functionality to enhance user convenience.
     - Enabled the function to enter vehicle ID and select the rental center name to manage vehicles.

2. Page Optimization and UI Design:
   - Optimized the home_operator.html page, transforming it from a simple original layout to a more modern design. The page now utilizes a four-flex layout, with responsive images and shadow effects, improving the visual appeal.
   - Changed the main image on the homepage and adjusted the layout.

3. Login and Registration Page Improvements:
   - Changed the background image of the login and registration pages and adjusted the CSS styles of the forms to meet modern design standards.
   - Optimized base.html, adjusted the width of the navigation bar, and applied overall styling improvements to the pages.

4. Feature Expansion:
   - Integrated Google Navigation functionality to help guests quickly locate nearby parking spots. A "Map Navigation" option was added to the guest services drop-down menu, allowing guests to see their location and nearby parking spots clearly. By clicking on the parking spot icon, they can jump to the Google Navigation page for quick directions, significantly improving customer experience and work efficiency.

5. Other Optimizations and Fixes:
   - Enhanced the password addition method and added a user mark in the extra function section.
   - Optimized base.html, login, registration, and homepage, improved background design and form styles, and upgraded the overall user experience.Although some parts were not included in the final version, the optimizations and modifications I made during the development process had an impact on the project. I learned a lot from these tasks and contributed to the improvements of the project.
