import json
from src.controllers.global_dicts import cars, customers, CARS_ID, CUSTOMERS_ID
from src.models.car import CarBuilder
from src.models.customer import CustomerBuilder
from src.views.menus import MainMenu


def load_initial_data():
    global CARS_ID
    global CUSTOMERS_ID
    try:
        with open('src/data/initial_data.json', 'r') as file:
            data = json.load(file)
            
            # Carregando carros
            for car_data in data['cars']:
                try:
                    car = (CarBuilder()
                        .com_id(CARS_ID)
                        .com_license_plate(car_data['plate'])
                        .com_brand(car_data['brand'])
                        .com_model(car_data['model'])
                        .com_year(car_data['year'])
                        .com_daily_rate(car_data['daily_rate'])  # Alterado de price para daily_rate
                        .build())  
                    cars[CARS_ID] = car
                    CARS_ID += 1
                except Exception as e:
                    print(f"Erro ao criar carro: {e}")
            # Carregando clientes
            for customer_data in data['customers']:
                try:
                    customer = (CustomerBuilder()
                        .com_email(customer_data['email'])
                        .com_name(customer_data['name'])
                        .com_wallet(customer_data['wallet'])
                        .com_password(customer_data.get('password', '123456'))  # Valor padrão se não existir
                        .com_id(CUSTOMERS_ID)
                        .build())
                    customers[customer_data['email']] = customer
                    CUSTOMERS_ID += 1
                except Exception as e:
                    print(f"Erro ao criar cliente: {e}")

            print("Dados iniciais carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar dados iniciais: {e}")

if __name__ == "__main__":
    try:
        load_initial_data()  # Carrega os dados iniciais
    except Exception as e:
        print(f"Erro ao carregar dados iniciais: {e}")
        exit()
    menu = MainMenu()    # Cria uma instância do menu principal
    menu.execute()       # Executa o menu principal