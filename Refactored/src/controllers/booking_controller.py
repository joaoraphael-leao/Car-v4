from src.controllers.global_dicts import bookings, BOOKINGS_ID
from src.controllers.global_dicts import cars
from src.controllers.global_dicts import customers
from src.controllers.customer_controller import login
from src.controllers.car_controller import show_available_cars
from src.models.booking import BookingBuilder
from src.utils.dates.py import validate_date

## Create booking
def create_booking():
    customer_email = login().email
    show_available_cars()

    car_id = input("Enter car ID to book: ")
    car = cars.get(car_id)
    if not car:
        print("Car not found.")
        return None
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    validate_date(start_date, end_date)
    ## calcular tempo em dias de reserva
    cost = calculate_booking_cost(car, start_date, end_date)
    booking = BookingBuilder()
    booking.com_car_id(car_id)
    booking.com_customer_email(customer_email)
    booking.com_start_date(start_date)
    booking.com_end_date(end_date)
    booking.com_cost(cost)
    booking.build()

    bookings[BOOKINGS_ID] = booking
    BOOKINGS_ID += 1
    
## Show bookings
def show_bookings():
    for booking in bookings:
        print(booking)

## Show booking by ID
def show_booking_by_id(booking_id):
    booking = bookings.get(booking_id)
    if not booking:
        print("Booking not found.")
        return None
    print(booking)

## Updates

## Update Booking
def update_booking():
    show_bookings()
    booking_id = input("Enter booking ID to update: ")
    booking = bookings.get(booking_id)
    if not booking:
        print("Booking not found.")
        return None
    customer_email = login().email
    if customer_email != booking.customer_email:
        print("You are not authorized to update this booking.")
        return None

    print("1. Update start date")
    print("2. Update end date")
    print("3. Update car")

    option = input("Select an option: ")
    if option == "1"
        new_start_date = input("Enter new start date (YYYY-MM-DD): ")
        try:
            validate_date(new_start_date, booking.end_date)
        except ValueError as e:
            print(e)
            return None

        booking.start_date = new_start_date
    elif option == "2":
        
        new_end_date = input("Enter new end date (YYYY-MM-DD): ")
        try:
            validate_date(booking.start_date, new_end_date)
        except ValueError as e:
            print(e)
            return None
        booking.end_date = new_end_date
    elif option == "3":
        show_available_cars()
        car_id = input("Enter new car ID: ")
        if car_id == booking.car_id:
            print("You have selected the same car.")
            return None
        car = cars.get(car_id)
        if not car:
            print("Car not found.")
            return None

        booking.car_id = car_id
    else:
        print("Invalid option.")
        return None
    
## Cancel Booking

## check car availability

## calculate booking cost
def calculate_booking_cost(car, start_date, end_date):
    # Assuming cost is per day
    days = (end_date - start_date).days
    return days * car.cost_per_day

def show_bookings_by_user(user_email):
    user_bookings = [booking for booking in bookings if booking.customer_email == user_email]
    if not user_bookings:
        print("No bookings found for this user.")
        return None
    for booking in user_bookings:
        print(booking)