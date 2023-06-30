# Flight Booking Web Application

This is a web application for flight ticket booking built with Django.

## Features

- User Login and Sign Up functionality
- Searching for flights based on date and time
- Booking tickets on available flights
- Viewing booked flights
- Admin login to manage flights

## Use Cases

### User Use Cases

- **Login**: Users can log in to their accounts to access the booking functionality.
- **Sign up**: New users can create an account with the required information.
- **Flight Search**: Users can search for flights based on date and time.
- **Ticket Booking**: Users can book tickets on available flights.
- **View Bookings**: Users can view their booked flights.
- **Logout**: Users can log out of their accounts.

### Admin Use Cases

- **Login**: Admin users can log in to the admin interface.
- **Add Flights**: Admin users can add new flights to the system.
- **Remove Flights**: Admin users can remove existing flights from the system.
- **View Bookings**: Admin users can view bookings based on flight number and time.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/syedhhassan/flight-booking.git
   ```
2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
- On MacOS
    ```bash
    source venv/bin/activate
    ```
- On Windows
    ```bash
    venv\Scripts\activate
    ```

4. Install the project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the development server:
    ```bash
    python3 manage.py runserver
    ```

6. Run the dockerfile:
- Building the Docker image
    ```bash
    docker build -t flight-booking-app .
    ```
- Running the Docker image
    ```bash
    docker run -p 8080:8000 flight-booking-app
    ```
- Stop the running container
    ```bash
    docker stop <container_name>
    ```
- Remove the container
    ```
    docker rm <container_name>
    ```

## Usage
- To access the user interface, open a web browser and go to `http://localhost:8000`
- To access the admin interface, go to `http://localhost:8000/admin` and log in with admin credentials.



