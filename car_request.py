import os
import classes
import car_management
import car_customer_list
import datetime
from geopy.geocoders import Nominatim

# Estrutura de dados mais completa para as requisições
requests = {}
user_input = ''

def get_coordinates_from_address(address):
    """
    Converte um endereço em coordenadas (latitude, longitude)
    """
    try:
        geolocator = Nominatim(user_agent="car_rental_system")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            print("Endereço não encontrado.")
            return None, None
    except Exception as e:
        print(f"Erro ao obter coordenadas: {e}")
        return None, None

def car_request_main():

    global user_input

    while user_input != '3':

        menu = classes.Request_Menu()
        menu.show_menu()
        menu.interact_menu()

        user_input = input("\n")

        # New Request
        if user_input == '1':

            os.system('cls')
            [print(f"ID: {key}\n\n{value}\n\n") for key, value in car_management.car_list.items()]

            car_request_id = input("Insert the ID of the car you want to request\n")

            if car_management.car_list[car_request_id].available.lower() == 'yes':

                os.system('cls')

                nickname = input("Insert your Nickname\n")
                
                # Coletar informações adicionais para o GPS tracking
                address = input("Insert the pickup address\n")
                start_date_str = input("Insert start date (DD/MM/YYYY)\n")
                end_date_str = input("Insert end date (DD/MM/YYYY)\n")
                
                # Converter strings de data para objetos datetime
                try:
                    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y")
                    end_date = datetime.datetime.strptime(end_date_str, "%d/%m/%Y")
                except ValueError:
                    print("Data inválida! Usando data atual como padrão.")
                    start_date = datetime.datetime.now()
                    end_date = start_date + datetime.timedelta(days=1)
                
                # Obter coordenadas do endereço
                latitude, longitude = get_coordinates_from_address(address)
                
                # Armazenar a requisição com informações completas
                requests[car_request_id] = {
                    'nickname': nickname,
                    'address': address,
                    'latitude': latitude,
                    'longitude': longitude,
                    'start_date': start_date,
                    'end_date': end_date,
                    'status': 'pending'  # pending, active, completed, cancelled
                }

                car_management.car_list[car_request_id].available = 'No'
                car_customer_list.customers_list[0].last_rent = car_request_id
                
                os.system('cls')
                print("Car successfully requested!\n")
                
                # Mostrar as coordenadas obtidas
                if latitude and longitude:
                    print(f"GPS coordinates: {latitude}, {longitude}")
                else:
                    print("Não foi possível obter coordenadas para o endereço fornecido.")
            
            elif car_management.car_list[car_request_id].available.lower() == 'no':
                os.system('cls')
                print("The car is already requested!\n")
        
        # Request Cancel
        elif user_input == '2':

            os.system('cls')
            [print(f"ID: {key}\n\n{value}\n\n") for key, value in car_management.car_list.items()]

            car_request_id = input("Insert the ID of the car you want to cancel the request\n")

            if car_management.car_list[car_request_id].available.lower() == 'no':
                os.system('cls')
                print("Car request successfully canceled!\n")

                car_management.car_list[car_request_id].available = "Yes"
                
                # Atualizar status da requisição se existir
                if car_request_id in requests:
                    requests[car_request_id]['status'] = 'cancelled'
            
            elif car_management.car_list[car_request_id].available.lower() == 'yes':
                os.system('cls')
                print("There is no request for this car!\n")
