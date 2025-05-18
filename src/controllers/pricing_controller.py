from src.controllers.global_dicts import cars, special_offers
from src.controllers.car_controller import show_cars

def update_car_price():
    """Update base price of a car"""
    show_cars()
    car_id = input("Enter the car ID to change the price: ")
    
    if car_id not in cars:
        print("Car not found")
        return
        
    try:
        new_price = float(input("Enter the new base price: "))
        cars[car_id].daily_rate = new_price
        print("Price updated successfully!")
    except ValueError:
        print("Invalid price")

def add_special_offer():
    """Add special offer to a car"""
    show_cars()
    car_id = input("Enter the car ID to add special offer: ")
    
    if car_id not in cars:
        print("Car not found")
        return
        
    try:
        special_price = float(input("Enter the special price: "))
        duration = input("Enter the offer duration (days): ")
        conditions = input("Enter the offer conditions: ")
        
        offer = {
            'special_price': special_price,
            'duration': duration,
            'conditions': conditions
        }
        
        special_offers[car_id] = offer
        cars[car_id].offer = f"Special Offer: R${special_price}\nConditions: {conditions}"
        print("Special offer added successfully!")
        
    except ValueError as e:
        print(f"Error adding special offer: {e}")

def show_special_offers():
    """Show all active special offers"""
    if not special_offers:
        print("\nNo active special offers")
        return
        
    print("\n=== Active Special Offers ===")
    for car_id, offer in special_offers.items():
        print(f"\nCar ID: {car_id}")
        print(f"Special Price: R${offer['special_price']}")
        print(f"Duration: {offer['duration']} days")
        print(f"Conditions: {offer['conditions']}")
        print("===========================")