from nt import error
from src.controllers.global_dicts import bookings, BOOKINGS_ID, feedbacks
from src.controllers.global_dicts import cars
from src.controllers.global_dicts import customers
from src.controllers.customer_controller import login
from src.controllers.car_controller import show_available_cars
from src.models.booking import BookingBuilder
from src.utils.dates import validate_date
from geopy.geocoders import Nominatim

def is_booking_active(booking):
    """
    Verifica se uma reserva está ativa no momento atual
    
    Args:
        booking: Objeto de reserva a ser verificado
        
    Returns:
        bool: True se a reserva estiver ativa, False caso contrário
    """
    from datetime import datetime
    
    today = datetime.now().date()
    
    if isinstance(booking.start_date, str):
        try:
            start_date = datetime.strptime(booking.start_date, "%Y-%m-%d").date()
        except ValueError:
            start_date = datetime.strptime(booking.start_date, "%d-%m-%Y").date()
    else:
        start_date = booking.start_date
        
    if isinstance(booking.end_date, str):
        try:
            end_date = datetime.strptime(booking.end_date, "%Y-%m-%d").date()
        except ValueError:
            end_date = datetime.strptime(booking.end_date, "%d-%m-%Y").date()
    else:
        end_date = booking.end_date
    
    return start_date <= today <= end_date

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
            print("Could not obtain coordinates for the provided address.")
            return None, None
    except Exception as e:
        print(f"Error obtaining coordinates: {e}")
        return None, None

def convert_date_format(date_str):
    """
    Converte a data para o formato YYYY-MM-DD independente do formato de entrada
    Aceita DD-MM-YYYY ou YYYY-MM-DD
    """
    from datetime import datetime
    
    # First try YYYY-MM-DD format
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str  # Already in the correct format
    except ValueError:
        pass
    
    # Try DD-MM-YYYY format
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj.strftime("%Y-%m-%d")  # Convert to YYYY-MM-DD
    except ValueError:
        # If no format works, guide the user
        print(f"Invalid date format: {date_str}. Use DD-MM-YYYY or YYYY-MM-DD")
        return date_str  # Return the original string so the error can be handled later

def create_booking():
    global BOOKINGS_ID
    customer = login()
    
    customer_email = customer.email
    
    print("Enter dates in format YYYY-MM-DD or DD-MM-YYYY")
    start_date = input("Enter start date: ")
    end_date = input("Enter end date: ")
    
    # Converter para formato YYYY-MM-DD se necessário
    start_date = convert_date_format(start_date)
    end_date = convert_date_format(end_date)

    try:
        validate_date(start_date, end_date)
    except ValueError as e:
        print(e)
        return None
    
    # Mostrar apenas carros disponíveis nesse período
    from src.controllers.car_controller import show_cars_available_by_date
    available_cars = show_cars_available_by_date(start_date, end_date)
    
    if not available_cars:
        return None
    
    car_id = int(input("Enter car ID to book: "))
    car = cars.get(car_id)
    
    # Continuar com o processo de reserva usando o builder
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

    booking.com_location(latitude, longitude)

    try:
        new_book = booking.build()
        bookings[BOOKINGS_ID] = new_book
        BOOKINGS_ID += 1
        print(f"Booking created successfully! ID: {BOOKINGS_ID-1}")
        print(new_book)
        
        # Adding simplified Rental Agreement
        rental_agreement = {
            "RENTAL AGREEMENT": {
                "Booking ID": BOOKINGS_ID-1,
                "Customer": customer_email,
                "Car ID": car_id,
                "Model": car.model,
                "License Plate": car.license_plate,
                "Start Date": start_date,
                "End Date": end_date,
                "Total Cost": f"${cost:.2f}",
                "Pickup Location": address,
                "Terms": [
                    "1. Customer responsible for damages",
                    "2. Return on agreed date",
                    "3. Traffic fines are customer's responsibility",
                    "4. Basic insurance included",
                    "5. Return with full tank"
                ]
            }
        }
        
        print("\n=== RENTAL AGREEMENT ===")
        print(rental_agreement)
        customer.add_debts(cost)
        return new_book
    except ValueError as e:
        print(e)
        return None

def show_bookings():
    for booking in bookings:
        print(booking)

def get_booking(booking_id):
    booking = bookings.get(booking_id)
    if not booking:
        raise error("Booking not found.")
    return booking

def show_booking_by_id():
    booking_id = int(input("Enter booking ID: "))
    try:
        booking = get_booking(booking_id)
        print(booking)
    except ValueError as error:
        print(error)
        return None

## Update Booking
def update_booking():
    show_bookings()
    booking_id = input("Enter booking ID to update: ")
    try:
        booking = get_booking(booking_id)
    except ValueError as error:
        print(error)
        return None
    
    customer = login()
    if customer.email != booking.customer_email:
        print("You are not authorized to update this booking.")
        return None

    print("1. Update start date")
    print("2. Update end date")
    print("3. Update car")

    option = input("Select an option: ")
    
    match option:
        case "1":
            new_start_date = input("Enter new start date (YYYY-MM-DD): ")
            try:
                validate_date(new_start_date, booking.end_date)
                booking.start_date = new_start_date
            except ValueError as e:
                print(e)
                return None
        case "2":
            new_end_date = input("Enter new end date (YYYY-MM-DD): ")
            try:
                validate_date(booking.start_date, new_end_date)
                booking.end_date = new_end_date
            except ValueError as e:
                print(e)
                return None
        case "3":
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
        case _:
            print("Invalid option.")
            return None

    print("Booking updated successfully.")

    
## Cancel Booking

## check car availability

## calculate booking cost
def calculate_booking_cost(car, start_date, end_date):
    from datetime import datetime
    
    # Convert string dates to datetime objects
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    days = (end_date - start_date).days
    return days * car.daily_rate

def show_bookings_by_user(user_email):
    user_bookings = [booking for booking in bookings if booking.customer_email == user_email]
    if not user_bookings:
        print("No bookings found for this user.")
        return None
    for booking in user_bookings:
        print(booking)

def give_feedback():
    user = login()
    if not user:
        return None
        
    show_bookings_by_user(user.email)
    booking_id = input("Enter booking ID to give feedback: ")
    booking = bookings.get(booking_id)
    if not booking:
        print("Booking not found.")
        return None
    if booking.customer_email != user.email:
        print("You are not authorized to give feedback for this booking.")
        return None
    rating = input("Enter your rating (1-5): ")
    feedback = input("Enter your feedback: ")
    feedback = {
        "user": user.email,
        "car": booking.car_id,
        "rating": rating,
        "feedback": feedback
    }
    feedbacks.append(feedback)
    print("Feedback given successfully.")
def show_feedbacks():
    for feedback in feedbacks:
        print(feedback)