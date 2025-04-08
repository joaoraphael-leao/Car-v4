from models.car import CarBuilder
from global_dicts import cars

def add_car(global_car__id):
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

    try:
        car = car.builder()
        car.set_id(global_car_id)   
        cars[global_car_id] = car
        print("Car added successfully")
    except ValueError as e:
        print(e)
        return
    
def correct_car_data(car_id):
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
    for car in cars.values():
        print(car)

def show_available_cars():
    for car in cars.values():
        if car.is_available:
            print(car)