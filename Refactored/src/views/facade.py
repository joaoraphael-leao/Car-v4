from src.controllers import car_controller, customer_controller, pricing_controller, booking_controller, report_controller, gps_controller, payment_controller
from src.controllers.customer_controller import login

#Car Facade
class CarFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.controller = car_controller
        return cls._instance

    def show_cars(self):
        self.controller.show_cars()
    
    def add_car(self):
        self.controller.add_car()
    
    def show_available_cars(self):
        self.controller.show_available_cars()

    def remove_cars(self):
        self.controller.remove_cars()
    
    def update_car(self):
        self.show_cars()
        car_id = int(input("Digite o ID do carro que deseja editar: "))
        self.controller.correct_car_data(car_id)
        
#Customer Facade
class CustomerFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.controller = customer_controller
        return cls._instance

    def add_customer(self):
        self.controller.add_customer()
    
    def show_customers(self):
        self.controller.show_customers()
    
    def find_customer(self):
        customer_email = input("Digite o email do cliente: ")  # Recebe o ID do cliente do usuário no teclado
        self.controller.find_customer(customer_email)
    
    def update_customer(self):
        self.controller.update_customer()

    def delete_customer(self):
        email = input("Digite o email do cliente a ser deletado: ")  # Recebe o ID do cliente do usuário no teclado
        self.controller.delete_customer(email)
    
#Pricing Facade 
class PricingFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.controller = pricing_controller
        return cls._instance
    
    def update_car_price(self):
        self.controller.update_car_price()
    
    def add_special_offer(self):
        self.controller.add_special_offer()

    def show_special_offers(self):
        self.controller.show_special_offers()

#Booking Facade
class BookingFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.controller = booking_controller
        return cls._instance
    
    def create_booking(self):
        self.controller.create_booking()
    
    def show_bookings(self):
        self.controller.show_bookings()
    
    def show_booking_by_id(self):
        self.controller.show_booking_by_id()
    
    def update_booking(self):
        self.controller.update_booking()

    def show_bookings_by_user(self):
        self.controller.show_bookings_by_user()
    
    def give_feedback(self):
        self.controller.give_feedback()

#Report Facade
class ReportFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.controller = report_controller
        return cls._instance
    
    def add_relatory(self):
        self.controller.add_relatory()
    
    def list_reports(self):
        self.controller.list_reports()
    
    def list_user_reports(self):
        self.controller.list_user_reports()
    
    def delete_relatory(self):
        self.controller.delete_relatory()

#GPS Facade
class GPSFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.controller = gps_controller
        return cls._instance

    def show_map(self):
        print("\nGenerating map with all cars...")
        self.controller.show_map()
        print("\nMap opened in your browser.")

#Payment Facade
class PaymentFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.controller = payment_controller
        return cls._instance

    def add_funds(self):
        customer = login()
        if not customer:
            return False
        amount = float(input("Digite o valor a ser adicionado: "))
        self.controller.add_funds(email=customer.email, amount=amount)
    
    def check_balance(self):
        customer = login()
        if not customer:
            return False
        self.controller.check_balance(customer.email)
    
    def pay_debts(self):
        customer = login()
        if not customer:
            return False
        self.controller.pay_debts(customer.email)
