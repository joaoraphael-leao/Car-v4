from abc import ABC, abstractmethod
import os

class Reports: 

    def __str__(self):
        return "Undefined"  

class Maintenance(Reports):
    
    def __init__(self, maintenance_date, maintenance_details,):
        self.maintenance_date = maintenance_date
        self.maintenance_details = maintenance_details
    
    def __str__(self):
        return f"{self.maintenance_date}: {self.maintenance_details}"   

class Service(Reports):
    
    def __init__(self, service_date, service_details):
        self.service_date = service_date
        self.service_details = service_details
    
    def __str__(self):
        return f"{self.service_date}: {self.service_details}"

class Damage(Reports):
    
    def __init__(self, damage_date, damage_details):
        self.damage_date = damage_date
        self.damage_details = damage_details
    
    def __str__(self):
        return f"{self.damage_date}: {self.damage_details}"

class Incident(Reports):
    
    def __init__(self, incident_date, incident_details):
        self.incident_date = incident_date
        self.incident_details = incident_details
    
    def __str__(self):
        return f"{self.incident_date}: {self.incident_details}"


class Customer:
    def __init__(self, nickname, id, name, debt, funds, reviews, last_rent):
        
        self.nickname = nickname
        
        self.__id = id
        self.__name = name
        
        self.debt = debt
        self.funds = funds
        self.reviews = reviews
        self.last_rent = last_rent
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        if not isinstance(new_id, int):
            raise TypeError("ID must be a number")
        if 1 < new_id <= 99999999999:
            self.__id = new_id
        else:
            raise ValueError("Invalid value for a ID")
        

    @property    
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("This is not a name")
        self.__name = new_name

    def __str__(self):
        return f"{self.nickname}\n\nID: {self.id}\nName: {self.name}\nDebt: R$ {self.debt}\nFunds: R$ {self.funds}\nLast Review: {self.reviews}\nLast Rent: {self.last_rent}\n"

class Vehicle(Reports):
    def __init__(self, brand, model, color, horse_power, price_day, available,maintenance_date, maintenance_details, service_date,
                  service_details, damage_date, damage_details, incident_date, incident_details, offer):
        
        self.brand = brand
        self.model = model
        self.color = color
        self.horse_power = horse_power
        self.price_day = price_day
        self.available = available

        self.maintenance_date = maintenance_date
        self.maintenance_details = maintenance_details

        self.service_date = service_date
        self.service_details = service_details

        self.damage_date = damage_date
        self.damage_details = damage_details

        self.incident_date = incident_date
        self.incident_details = incident_details 

        self.offer = offer

    def Availability(self):
        return self.available
        
    
    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nColor: {self.color}\nHP: {self.horse_power} HP\nPrice(day): R${self.price_day}/day\nAvailable: {self.available}\nLast Maintenance Record: {self.maintenance_date} {self.maintenance_details}\nLast Service Record: {self.service_date} {self.service_details}\nLast Damage Reported: {self.damage_date} {self.damage_details}\nLast Incident Reported: {self.incident_date} {self.incident_details}\nOffers: {self.offer}"



class Menus(ABC):

    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def interact_menu(self):
        pass


class Menu_Selector(Menus):
    def show_menu(self):
        print("Main menu\n")
    
    def interact_menu(self):
        print("1. Car Management Menu")
        print("2. Profile Menu")
        print("3. Car Request Menu")
        print("4. Car Report Menu")
        print("5. Payment Processing Menu")
        print("6. Rental Agreements Menu")
        print("7. Pricing and Offers Menu")
        
class Management_Menu(Menus):

    def show_menu(self):
        print("Car Management Menu\n\n")

    def interact_menu(self):
        print("1. Add")
        print("2. See")
        print("3. Exit")

class Customer_Menu(Menus):

    def show_menu(self):
        print('Profile Menu\n\n')
    
    def interact_menu(self):
        print("1. Add")
        print("2. See")
        print("3. Exit")

class Request_Menu(Menus):

    def show_menu(self):
        print('Car Request Menu\n\n')

    def interact_menu(self):
        print('1. Make a new Request')
        print('2. Cancel Request')
        print('3. Exit')

class Payment_Processing_Menu(Menus):

    def show_menu(self):
        print("Payment Processing Menu\n\n")
    
    def interact_menu(self):
        print('1. Payment')
        print('2. Deposit')
        print('3. Refund')
        print('4. Exit')

class Car_Rental_Agreement_Menu(Menus):

    def show_menu(self):
        print("Rental Agreements Menu\n")

    def interact_menu(self):
        print('1. Make a new agreement')
        print('2. Cancel an agreement')
        print('3. See Agreements')
        print('4. Exit')

class Car_Pricing_And_Offers_Menu(Menus):

    def show_menu(self):
        print("Pricing and Special Offers Menu\n")

    def interact_menu(self):
        print('1. Manage Pricing and Special Offers')
        print('2. See Pricing and Special Offers')

class Car_Customer_Feedback_And_Reviews_Menu(Menus):
    
    def show_menu(self):
        print('User Feedback and Review Menu\n')
    
    def interact_menu(self):
        print('1. Submit Feedback and Review')
        print('2. See Feebacks and Reviews')
        print('3. Exit')

class Car_Reports_Management_Menu(Menus):

    def show_menu(self):
        print("Reports Menu\n")

    def interact_menu(self):
        print('1. Maintenance Menu')
        print('2. Service Menu')
        print('3. Damage Menu')
        print('4. Incident Menu')
        print('5. Exit')

    def maintenance_submenu_header(self):
        print('Maintenance Menu\n')
    
    def maintenance_submenu(self):
        print('1. Add new maintenance report')
        print('2. See maintenance record')
        print('3. Return')
    
    def service_submenu(self):
        print('1. Add new service report')
        print('2. See service record')
        print('3. Return')

    def damage_submenu(self):
        print('1. Add new damage report')
        print('2. See damage record')
        print('3. Return')

    def incident_submenu(self):
        print('1. Add new incident report')
        print('2. See incident record')
        print('3. Return')
        

