# 🚗 Car Rental System

## 🚀 Como Executar o Projeto

1. **Pré-requisitos**
   - Python 3.7 ou superior
   - Bibliotecas: geopy, folium (para o sistema de GPS)

2. **Passos para Execução**
   - Clone o repositório para sua máquina local

   - Instale as dependências necessárias:
     ```
     pip install geopy folium
     ```
   - Execute o programa principal:
     ```
     python main.py
     ```

## 📋 Overview

## ✨ Functionalities
- **🚙 Vehicle Inventory Management**
    - Class of Car implemented in 'src/models/car.py'
    - Controller of Car implemented in'src/controllers/car_controller.py'
    - Implemented.
- **📅 Reservation System**
    - _Users can book cars_
    -  Class of Booking implemented in 'src/models/booking.py'
    - Controller of Booking implemented in'src/controllers/booking_controller.py'
    - Implemented.

- **👤 Customer Profile Management**
    _Users can create an account to book cars._
    - Class of Customer implemented in'src/models/customer.py'
    - Controller of Customer implemented in'src/controllers/customer_controller.py'
    - Implemented.

- **💰 Payment Processing**
    - _Users can pay for the booking._
    - Payment and wallet system implemented inside the Customer class.
    - We have the attribute 'wallet' in the Customer class.
    - And the methods 'pay', 'has_debts', 'add_debts', 'wallet_get', 'wallet_add'.
    - Implemented.

- **📝 Rental Agreement Management**
    - Implemented in the time you book a car...
- **🗺️ GPS and Vehicle Tracking**
    - Implemented in the file 'src/controllers/gps_controller.py', using the library 'geopy' and folium.
    - We use the attributes 'latitude' and 'longitude' in the Booking class, 
    so we can track where the customer who rent the car is.
    - I cannot put a real GPS in the project because i don't have real cars to update.
    - If i would implement it, i would put the method 'drive' in the Car class or Booking,
    with parameters ('direction', 'distance') and update the attributes 'latitude' and 'longitude'
    - But it wouldn't be real.
    - Implemented.

- **🔧 Mainteance and Service Records**
   - Implemented with the classes 'Reports' and 'Service' in 'src/models/reports.py'.
   - We can use the 'reports_controller.py' to interact with the reports class.
   - Implemented.

- **💲 Pricing and Special Offers**
    - Implemented Car Price in the own Car class.
    - Implemented.

- **🚨 Damage and Incident Reporting**
- We use the class 'Reports' in'src/models/reports.py'.
    - Implemented.

- **⭐ Customer Feedback and Reviews**
    - Partially implemented with just a dictionary in 'customer_controller.py'
    - Implemented.

## 🧩 Object Oriented Programming (OOP)
- **🧠 Abstraction**
    - Implemented in 'src/views/menus.py'.
    - We have a general menu class with the abstract methods 'show_menu' and 'process_choice'.

- **🔒 Encapsulation**
    - Implemented in the models folder.
    - We use Encapsulation to hide sensible data from the attributes of the classes.

- **👪 Inheritance**
    - Implemented in the menus, where the specific menus inherit from the general menu class.
    - Implemented in the Report class, where the Services is a subclass of Reports with
    additional attribute cost.

- **🔄 Polymorphism**
    - Implemented in the menus file: 'src/views/menus.py', where the specific menus inherit from the general menu class.

## 🏗️ Project Patterns 
    - Creational Pattern
        - 🏗️ Builder Pattern
           - Problem: Controllers was with a lot of conditions to create a new object, 
           and it was hard to read, maintain and upgrade.
           - Solution: We used the Builder Pattern to validate these conditions in the Builder
           class only, so the Controllers are more readable and easier to maintain.
           - Location
            - Files of 'src/models'
        
        - 🔄 Singleton Pattern
            - Problem: In menus.py, every time we use the method "process choice" of a submenu, we create a new instance of
            the submenu own facade, so we have a lot of instances of
            the same submenu facade.
            - Solution: We used the Singleton Pattern to create a unique instance of every submenu facade.
            - Location
            - File of 'src/views/facade.py'
    
    - Structural Pattern
        - 🏢 Facade Pattern
            - Problem: Menus directly interact with the controllers, so, every time we want change the controller, we need to change the menu.
            - Solution: We used the Facade pattern to create a Facade as a layer between the menu and the controller, so, if we change the controller, we only need to change the facade.
            - Location
            - File of'src/views/facade.py'

    - Behavioral Pattern
        - 📋 Template Method Pattern
            - Problem: Duplicated code in the execution menus, and we didn't had a padronized way to execute the menus, every submenu has their own flow.
            - Solution: We used the Template Method Pattern to create a template method in the general menu class, so, every submenu has the same flow.
            - Orquestrador: Execute Menu
            - Hotspots:
                - Show Menu
                - Process Choice  
            - Location
            - File of'src/views/menus.py'
