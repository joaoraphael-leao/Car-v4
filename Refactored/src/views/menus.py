from abc import ABC, abstractmethod
from src.controllers.car_controller import add_car, show_cars, show_available_cars, correct_car_data



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


submenu_classes = {
    1: CarMenu,
    #2: "CustomerManagementMenu",
    #3: "BookingManagementMenu",
    #4: "ReportManagementMenu",
    #5: "PaymentProcessingMenu",
    #6: "RentalAgreementMenu",
    #7: "PricingAndOffersMenu",
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


