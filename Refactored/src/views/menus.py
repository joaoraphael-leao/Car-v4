from abc import ABC, abstractmethod

submenu_classes = {
    1: CarManagementMenu,
    2: CustomerManagementMenu,
    3: BookingManagementMenu,
    4: ReportManagementMenu,
    5: PaymentProcessingMenu,
    6: RentalAgreementMenu,
    7: PricingAndOffersMenu,
    8: CarTrackingMenu
}
def display(options):
        
        
        
        for key, value in options.items():
            print(f"{key}) {value}")
            
        
        print("="*50)

class Menu(ABC):
    """
    Classe abstrata base para todos os submenus do sistema.
    """
    def __init__(self):
        self.options = {}
    def show_menu(self):
        
        pass

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
        submenu.process()


class SubMenu(Menu):
    """
    Classe base para todos os submenus do sistema.
    """
    def __init__(self, title):
        self.title = title
        self.options = {}
    
    def display(self):
        """
        Exibe o submenu. 
        """
        print("\n" + "="*50)
        print(f"{self.title}".center(50))
        print("="*50)
        
        for key, value in self.options.items():
            print(f"{key}. {value}")
        
        print("0. Return to Main Menu")
        print("="*50)
    
    def get_user_choice(self):
        """
        Obtém a escolha do usuário.
        
        Returns:
            int: A opção escolhida pelo usuário
        """
        max_option = max(self.options.keys())
        while True:
            try:
                choice = int(input(f"Enter your choice (0-{max_option}): "))
                if 0 <= choice <= max_option:
                    return choice
                else:
                    print(f"Invalid choice. Please enter a number between 0 and {max_option}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    @abstractmethod
    def process_choice(self, choice):
        """
        Processa a escolha do usuário.
        
        Args:
            choice (int): A opção escolhida pelo usuário
        """
        pass
    
    def show_menu(self):
        """
        Exibe o submenu e processa a escolha do usuário.
        """
        while True:
            self.display()
            choice = self.get_user_choice()
            
            if choice == 0:
                print("Returning to Main Menu...")
                break
            
            self.process_choice(choice)