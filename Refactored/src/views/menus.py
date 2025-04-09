from abc import ABC, abstractmethod
from src.controllers.car_controller import add_car, show_cars, show_available_cars, correct_car_data
from src.controllers.pricing_controller import update_car_price, add_special_offer, show_special_offers
from src.controllers.booking_controller import (create_booking, show_bookings, 
    show_booking_by_id, update_booking, show_bookings_by_user, give_feedback)
from src.controllers.report_controller import add_relatory, list_reports, list_user_reports, delete_relatory
from src.controllers.customer_controller import add_customer, show_customers, find_customer, update_customer, delete_customer

class Menu(ABC):
    """
    Classe abstrata base para todos os submenus do sistema.
    """
    @abstractmethod
    def show_menu(self):
        raise NotImplementedError
    
    @abstractmethod
    def process_choice(self, choice):
        raise NotImplementedError
class CarMenu(Menu):

    def show_menu(self):
        print("Car Management Menu")
        print("1. Add Car")
        print("2: List All Cars")
        print("3 List Available Cars")
        print("4. Update Car")
        print("5. Exit")
        return
    
    def process_choice(self, choice):
        if choice == 1:
            add_car()
        elif choice == 2:
            show_cars()
        elif choice == 3:
            show_available_cars()
        elif choice == 4:
            show_cars()
            car_id = int(input("Enter the ID of the car you want to update: "))
            correct_car_data(car_id)
        elif choice == 5:
            return "exit"
        return None

class CustomerMenu(Menu):
    def show_menu(self):
        print("\n=== Customer Management Menu ===")
        print("1. Add Customer")
        print("2. Show All Customers")
        print("3. Find Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Exit")
    
    def process_choice(self, choice):
        if choice == 1:
            add_customer()
        elif choice == 2:
            show_customers()
        elif choice == 3:
            email = input("Enter customer email: ")
            find_customer(email)
        elif choice == 4:
            update_customer()
        elif choice == 5:
            email = input("Enter customer email to delete: ")
            delete_customer(email)
        elif choice == 6:
            return "exit"
        return None


class PricingMenu(Menu):
    def display(self):
        print("\n=== Gerenciamento de Preços e Ofertas ===")
        print("1. Atualizar Preço Base")
        print("2. Adicionar Oferta Especial")
        print("3. Visualizar Ofertas Especiais")
        print("4. Voltar")
        
    def process_choice(self):
        choice = input("Escolha uma opção: ")
            
        if choice == "1":
            update_car_price()
        elif choice == "2":
            add_special_offer()
        elif choice == "3":
            show_special_offers()
        elif choice == "4":
            return "exit"
        else:
            print("Opção inválida!")
        return None

class BookingMenu(Menu):
    def show_menu(self):
        print("\n=== Booking Management Menu ===")
        print("1. Create Booking")
        print("2. Show All Bookings")
        print("3. Show Booking by ID")
        print("4. Update Booking")
        print("5. Show My Bookings")
        print("6. Give Feedback")
        print("7. Exit")
    
    def process_choice(self, choice):
        if choice == 1:
            create_booking()
        elif choice == 2:
            show_bookings()
        elif choice == 3:
            booking_id = input("Enter booking ID: ")
            show_booking_by_id(booking_id)
        elif choice == 4:
            update_booking()
        elif choice == 5:
            email = input("Enter your email: ")
            show_bookings_by_user(email)
        elif choice == 6:
            give_feedback()
        elif choice == 7:
            return "exit"
        return None

class ReportMenu(Menu):
    def show_menu(self):
        print("\n=== Report Management Menu ===")
        print("1. Add Report")
        print("2. List All Reports")
        print("3. List My Reports")
        print("4. Delete Report")
        print("5. Exit")
    
    def process_choice(self, choice):
        if choice == 1:
            add_relatory()
        elif choice == 2:
            list_reports()
        elif choice == 3:
            email = input("Enter your email: ")
            list_user_reports(email)
        elif choice == 4:
            delete_relatory()
        elif choice == 5:
            return "exit"
        return None

submenu_classes = {
    1: CarMenu,
    2: CustomerMenu,
    3: BookingMenu,
    4: ReportMenu,
    #5: "PaymentProcessingMenu", 
    #6: RentalAgreementMenu,
    7: PricingMenu,
    #8: "CarTrackingMenu"
}

class MainMenu:
    """
    Menu principal do sistema de aluguel de carros.
    """
    def __init__(self):
        self.options = {
            1: "Car Management",
            2: "Customer Management",
            3: "Booking Management",
            4: "Report Management",
            5: "Payment Processing",
            6: "Rental Agreements",
            7: "Pricing and Offers",
            8: "Car Tracking",
            9: "Exit"
        }
    
    def display(self):
        """
        Exibe o menu principal.
        """
        print("\n" + "="*50)
        print("CAR RENTAL SYSTEM - MAIN MENU".center(50))
        print("="*50)
        
        for key, value in self.options.items():
            print(f"{key}) {value}")
        
        print("="*50)
    
    def get_user_choice(self):
        """
        Obtém a escolha do usuário.
        
        Returns:
            int: A opção escolhida pelo usuário
        """
        while True:
            try:
                choice = int(input("Enter your choice (1-9): "))
                if 1 <= choice <= 9:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 9."  )
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def execute(self):
        """
        Executa o menu principal em um loop até que o usuário escolha sair.
        """
        while True:
            self.display()
            choice = self.get_user_choice()
            
            if choice == 9:
                print("Thank you for using the Car Rental System. Goodbye!")
                break
            
            self.process_choice(choice)
    
    def process_choice(self, choice):
        """
        Processa a escolha do usuário.
        
        Args:
            choice (int): A opção escolhida pelo usuário
        """
        submenu = submenu_classes[choice]()
        submenu.show_menu()
        choice = int(input("Enter your choice: "))
        submenu.process_choice(choice)


