from src.controllers.global_dicts import bookings, BOOKINGS_ID, feedbacks
from src.controllers.global_dicts import cars
from src.controllers.global_dicts import customers
from src.controllers.customer_controller import login
from src.controllers.car_controller import show_available_cars
from src.models.booking import BookingBuilder
from src.utils.dates import validate_date
from geopy.geocoders import Nominatim


def get_coordinates_from_address(address):
    """
    Converte um endereço em coordenadas (latitude e longitude)
    """
    try:
        geolocator = Nominatim(user_agent="car_rental_system")
        location = geolocator.geocode(address)
        
        if location:
            return location.latitude, location.longitude
        else:
            print("Não foi possível obter coordenadas para o endereço fornecido.")
            return None, None
    except Exception as e:
        print(f"Erro ao obter coordenadas: {e}")
        return None, None

## Create booking
def create_booking():
    global BOOKINGS_ID
    customer = login()
    customer_email = customer.email
    show_available_cars()

    car_id = int(input("Enter car ID to book: "))
    car = cars.get(car_id)
    if not car:
        print("Car not found.")
        return None
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    validate_date(start_date, end_date)

    cost = calculate_booking_cost(car, start_date, end_date)
    booking = BookingBuilder()
    booking.com_car_id(car_id)
    booking.com_customer_email(customer_email)
    booking.com_start_date(start_date)
    booking.com_end_date(end_date)
    booking.com_cost(cost)
    booking.com_id(BOOKINGS_ID)

    address = input("Enter pickup/dropoff address: ")
    latitude, longitude = get_coordinates_from_address(address)

    if latitude and longitude:
        booking.com_location(longitude, latitude)
        print(f"Localização definida: {latitude}, {longitude}")
    else:
        print("Aviso: Não foi possível definir coordenadas para este endereço.")

    new_book = booking.build()

    bookings[BOOKINGS_ID] = new_book
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
    if option == "1":
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
    from datetime import datetime
    
    # Convert string dates to datetime objects
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    days = (end_date - start_date).days
    # Use daily_rate instead of cost_per_day to match the Car class property
    return days * car.daily_rate

def show_bookings_by_user(user_email):
    user_bookings = [booking for booking in bookings if booking.customer_email == user_email]
    if not user_bookings:
        print("No bookings found for this user.")
        return None
    for booking in user_bookings:
        print(booking)

def give_feedback():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email not in customers or customers[email].password != password:
        print("Invalid email or password.")
        return None
    show_bookings_by_user(email)
    booking_id = input("Enter booking ID to give feedback: ")
    booking = bookings.get(booking_id)
    if not booking:
        print("Booking not found.")
        return None
    if booking.customer_email != email:
        print("You are not authorized to give feedback for this booking.")
        return None
    rating = input("Enter your rating (1-5): ")
    feedback = input("Enter your feedback: ")
    feedback = {
        "user": email,
        "car": booking.car_id,
        "rating": rating,
        "feedback": feedback
    }
    feedbacks.append(feedback)

def show_feedbacks():
    for feedback in feedbacks:
        print(feedback)