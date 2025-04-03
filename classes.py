from abc import ABC, abstractmethod
import os

class Reports: 

    def __str__(self):
        return "Undefined"  

class Maintenance(Reports):
    
    def __init__(self, car_id, maintenance_date, maintenance_details):

        self.car_id = car_id
        self.maintenance_date = maintenance_date
        self.maintenance_details = maintenance_details
        
    
    def __str__(self):
        return f"Car ID: {self.car_id}\nReport type: Maintenance\n{self.maintenance_date}: {self.maintenance_details}\n"   

class Service(Reports):
    
    def __init__(self, car_id, service_date, service_details):
        
        self.car_id = car_id
        self.service_date = service_date
        self.service_details = service_details
    
    def __str__(self):
        return f"Car ID: {self.car_id}\nReport type: Service\n{self.service_date}: {self.service_details}\n"

class Damage(Reports):
    
    def __init__(self, car_id, damage_date, damage_details):
        
        self.car_id = car_id
        self.damage_date = damage_date
        self.damage_details = damage_details
    
    def __str__(self):
        return f"Car ID: {self.car_id}\nReport type: Damage\n{self.damage_date}: {self.damage_details}\n"

class Incident(Reports):
    
    def __init__(self, car_id, incident_date, incident_details):

        self.car_id = car_id
        self.incident_date = incident_date
        self.incident_details = incident_details
    
    def __str__(self):
        return f"Car ID: {self.car_id}\nReport type: Incident\n{self.incident_date}: {self.incident_details}\n"


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
        print("8. Car Tracking Menu")
        
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
        print('5. See Report History')
        print('6. Exit')

    def maintenance_submenu_header(self):
        print('Maintenance Menu\n')
    
    def maintenance_submenu(self):
        print('1. Add new maintenance report')
        print('2. Return')
    
    def service_submenu_header(self):
        print('Service Menu\n')

    def service_submenu(self):
        print('1. Add new service report')
        print('2. Return')

    def damage_submenu_header(self):
        print('Damage Menu\n')
    
    def damage_submenu(self):
        print('1. Add new damage report')
        print('2. Return')

    def incident_submenu_header(self):
        print('Incident Menu\n')
    
    def incident_submenu(self):
        print('1. Add new incident report')
        print('2. Return')

    def record_history_header(self):
        print('Record History\n')
        

class GPS_Tracking:
    def __init__(self, car_id, latitude=0.0, longitude=0.0, status="inactive"):
        self.car_id = car_id
        self.latitude = latitude
        self.longitude = longitude
        self.last_update = None
        self.status = status  # 'active', 'inactive', 'maintenance'
        self.tracking_history = []
        
        # Informações adicionais para integração com sistema de reservas
        self.reservation_id = None
        self.reservation_start = None
        self.reservation_end = None
        self.address = None
        self.brand = None
        self.model = None
    
    def update_location(self, latitude, longitude, timestamp=None):
        import datetime
        
        if timestamp is None:
            timestamp = datetime.datetime.now()
            
        # Atualizar localização atual
        self.latitude = latitude
        self.longitude = longitude
        self.last_update = timestamp
        
        # Adicionar ao histórico
        self.tracking_history.append({
            'timestamp': timestamp,
            'latitude': latitude,
            'longitude': longitude
        })
    
    def activate(self):
        self.status = "active"
    
    def deactivate(self):
        self.status = "inactive"
    
    def set_maintenance(self):
        self.status = "maintenance"
    
    def get_current_location(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'last_update': self.last_update,
            'status': self.status
        }
    
    def get_tracking_history(self):
        return self.tracking_history
    
    def calculate_distance_traveled(self):
        from geopy.distance import geodesic
        
        if len(self.tracking_history) < 2:
            return 0
        
        total_distance = 0
        for i in range(1, len(self.tracking_history)):
            point1 = (self.tracking_history[i-1]['latitude'], self.tracking_history[i-1]['longitude'])
            point2 = (self.tracking_history[i]['latitude'], self.tracking_history[i]['longitude'])
            total_distance += geodesic(point1, point2).kilometers
        
        return total_distance
    
    def generate_map(self, filename="vehicle_map.html"):
        """Gera um mapa com a localização atual e histórico"""
        import folium
        import os
        
        # Criar mapa centrado na localização atual
        map = folium.Map(location=[self.latitude, self.longitude], zoom_start=14)
        
        # Determinar cor com base no status
        marker_color = 'green' if self.status == 'active' else 'red'
        
        # Adicionar marcador para posição atual com ícone de carro
        folium.Marker(
            [self.latitude, self.longitude],
            popup=f"Car ID: {self.car_id}<br>Status: {self.status}",
            icon=folium.Icon(color=marker_color, icon='car', prefix='fa')
        ).add_to(map)
        
        # Adicionar linha para o histórico de rastreamento
        if len(self.tracking_history) > 1:
            points = [(entry['latitude'], entry['longitude']) for entry in self.tracking_history]
            folium.PolyLine(points, color="blue", weight=2.5, opacity=0.7).add_to(map)
        
        # Salvar o mapa
        map_path = os.path.join(os.path.dirname(__file__), filename)
        map.save(map_path)
        return map_path
    
    def __str__(self):
        status_text = "Ativo" if self.status == "active" else "Inativo" if self.status == "inactive" else "Em manutenção"
        reservation_text = f"Reserva: {self.reservation_id} (Início: {self.reservation_start}, Fim: {self.reservation_end})" if self.reservation_id else "Sem reserva"
        return f"Rastreamento do Carro ID: {self.car_id} ({self.brand} {self.model})\nStatus: {status_text}\nLocalização: {self.latitude}, {self.longitude}\nEndereço: {self.address}\n{reservation_text}\nÚltima atualização: {self.last_update}"


class Car_GPS_Tracking_Menu(Menus):
    def show_menu(self):
        print("GPS e Rastreamento de Veículos\n")
    
    def interact_menu(self):
        print('1. Iniciar Rastreamento')
        print('2. Parar Rastreamento')
        print('3. Ver Localização Atual')
        print('4. Ver Histórico de Rastreamento')
        print('5. Visualizar Mapa')
        print('6. Sair')