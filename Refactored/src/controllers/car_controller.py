from src.models.car import CarBuilder
from src.controllers.global_dicts import cars, CARS_ID


def show_cars_available_by_date(start_date, end_date):
    """
    Mostra os carros disponíveis em um intervalo de datas específico
    
    Args:
        start_date (str): Data de início no formato YYYY-MM-DD
        end_date (str): Data de fim no formato YYYY-MM-DD
        
    Returns:
        list: Lista de carros disponíveis no período
    """
    from datetime import datetime
    from src.controllers.global_dicts import cars, bookings
    from src.utils.dates import validate_date
    
    # Validar as datas
    validate_date(start_date, end_date)
    
    # Converter para objetos datetime
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    
    available_cars = []
    
    for car_id, car in cars.items():
        # Verificar se o carro está marcado como disponível
        if not car.is_available:
            continue
        
        # Verificar se o carro tem reservas que se sobrepõem ao período solicitado
        is_booked = False
        for booking_id, booking in bookings.items():
            if booking.car_id != car_id:
                continue
                
            # Converter datas da reserva
            booking_start = booking.start_date
            booking_end = booking.end_date
            
            if isinstance(booking_start, str):
                booking_start = datetime.strptime(booking_start, "%Y-%m-%d").date()
            if isinstance(booking_end, str):
                booking_end = datetime.strptime(booking_end, "%Y-%m-%d").date()
            
            # Verificar sobreposição de datas
            if (start_date <= booking_end and end_date >= booking_start):
                is_booked = True
                break
        
        if not is_booked:
            available_cars.append(car)
    
    if not available_cars:
        print(f"Não há carros disponíveis no período de {start_date} a {end_date}.")
    else:
        print(f"\nCarros disponíveis no período de {start_date} a {end_date}:")
        for car in available_cars:
            print(car)
            print("-" * 30)
    
    return available_cars
    
def add_car():
    global CARS_ID
    car = CarBuilder()
    brand = input("What is the car's brand? ")
    car.com_brand(brand)

    model = input("What is the car's model? ")
    car.com_model(model)

    year = int(input("What is the car's year? "))
    car.com_year(year)

    license_plate = input("What is the car's license plate? ")
    car.com_license_plate(license_plate)

    daily_rate = int(input("What is the car's daily rate? "))
    car.com_daily_rate(daily_rate)

    is_available = input("Is the car available? (y/n) ")
    is_available = True if is_available == "y" else False
    car.com_availability(is_available)

    car.com_id(CARS_ID)
    print(car,"\nid: ", CARS_ID)
    try:
        built_car = car.builder()
        cars[CARS_ID] = built_car
        print("Car added successfully")
        CARS_ID += 1
    except ValueError as e:
        print(e)
        return
    
def correct_car_data(car_id):
    
    if car_id not in cars: 
        print("Car not found")
        return
        
    print("What do you want to change?")
    print("1. Brand")
    print("2. Model")
    print("3. Year")
    print("4. License plate")
    print("5. Daily rate")
    
    option = int(input())

    if option == 1:
        brand = input("What is the car's brand? ")
        cars[car_id].brand = brand
    elif option == 2:
        model = input("What is the car's model? ")
        cars[car_id].model = model
    elif option == 3:
        year = int(input("What is the car's year? "))
        cars[car_id].year = year
    elif option == 4:
        license_plate = input("What is the car's license plate? ")
        cars[car_id].license_plate = license_plate
    elif option == 5:
        daily_rate = int(input("What is the car's daily rate? "))
        cars[car_id].daily_rate = daily_rate
    else:
        print("Invalid option")
        return
    
def show_cars():
    print("==========================")
    print("===== All registered cars =====")
    for car in cars.values():
        print(car)
        print("==========================")
    print("==========================")


def show_available_cars():
    for car in cars.values():
        if car.is_available:
            print(car)