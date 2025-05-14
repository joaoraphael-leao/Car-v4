from abc import ABC, abstractmethod
from src.views.facade import CarFacade, CustomerFacade, BookingFacade, ReportFacade, PricingFacade, GPSFacade, ReportFacade
class Menu(ABC):
    """
    Classe abstrata base para todos os submenus do sistema.
    """
    ## Template Method, execute_menu sendo um orquestrador da lógica
    def execute_menu(self):  # Método template
        while True:
            self.show_menu()  # Hotspot
            choice = self.get_user_input()  # Hook
            result = self.process_choice(choice)  # Hotspot
            if result == "exit":
                break
    
    @abstractmethod
    def show_menu(self):
        raise NotImplementedError
    
    @abstractmethod
    def process_choice(self, choice):
        raise NotImplementedError
    
    def get_user_input(self):  # Hook method
        return int(input("Digite sua escolha: "))
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
        facade = CarFacade()
        if choice == 1:
            facade.add_car()
        elif choice == 2:
            facade.show_cars() 
        elif choice == 3:
            facade.show_available_cars()
        elif choice == 4:
            facade.update_car()
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
        facade = CustomerFacade()
        if choice == 1:
            facade.add_customer()
        elif choice == 2:
            facade.show_customers()
        elif choice == 3:
            facade.find_customer()
        elif choice == 4:
            facade.update_customer()
        elif choice == 5:
            facade.delete_customer()
        elif choice == 6:
            return "exit"
        return None


class PricingMenu(Menu):
    def show_menu(self):
        print("\n=== Gerenciamento de Preços e Ofertas ===")
        print("1. Atualizar Preço Base")
        print("2. Adicionar Oferta Especial")
        print("3. Visualizar Ofertas Especiais")
        print("4. Voltar")
        
    def process_choice(self, choice):
        facade = PricingFacade()
        if choice == "1":
            facade.update_car_price()
        elif choice == "2":
            facade.add_special_offer()
        elif choice == "3":
            facade.show_special_offers()
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
        facade = BookingFacade()
        if choice == 1:
            facade.create_booking()
        elif choice == 2:
            facade.show_bookings()
        elif choice == 3:
            facade.show_booking_by_id()
        elif choice == 4:
            facade.update_booking()
        elif choice == 5:
            facade.show_bookings_by_user()
        elif choice == 6:
            facade.give_feedback()
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
        facade = ReportFacade()
        if choice == 1:
            facade.add_relatory()
        elif choice == 2:
            facade.list_reports()
        elif choice == 3:
            facade.list_user_reports()
        elif choice == 4:
            facade.delete_relatory()
        elif choice == 5:
            return "exit"
        return None

class GPSMenu(Menu):
    def show_menu(self):
        print("\n=== GPS Tracking Menu ===")
        print("1. Show All Cars on Map")
        print("2. Exit")
    
    def process_choice(self, choice):
        facade = GPSFacade()
        if choice == 1:
            facade.show_map()
        elif choice == 2:
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
    8: GPSMenu
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
        submenu.execute_menu()


