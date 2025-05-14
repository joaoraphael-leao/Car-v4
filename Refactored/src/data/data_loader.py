import json 
import os
from src.models.customer import CustomerBuilder
from src.controllers.global_dicts import customers, CUSTOMERS_ID

def load_customers():
    """
    Carrega os dados dos clientes do arquivo JSON e atualiza o contador global
    """
    global CUSTOMERS_ID
    
    json_path = os.path.join("src", "data", "customers.json")
    
    try:
        with open(json_path, "r", encoding='utf-8') as file:
            data = json.load(file)
            
        if not isinstance(data, list):
            raise ValueError("O arquivo JSON deve conter uma lista de clientes")
            
        for customer_data in data:
            # Validação dos campos obrigatórios
            required_fields = ["email", "name", "wallet", "password"]
            if not all(field in customer_data for field in required_fields):
                print(f"Aviso: Cliente com dados incompletos ignorado: {customer_data}")
                continue
                
            try:
                customer = (CustomerBuilder()
                          .com_email(customer_data["email"])
                          .com_name(customer_data["name"])
                          .com_wallet(float(customer_data["wallet"]))
                          .com_password(customer_data["password"])
                          .com_id(CUSTOMERS_ID)
                          .build())
                
                customers[customer_data["email"]] = customer
                CUSTOMERS_ID += 1
                
            except (ValueError, TypeError) as e:
                print(f"Erro ao criar cliente {customer_data.get('name', 'desconhecido')}: {str(e)}")
                continue
                
        print(f"Carregados {len(customers)} clientes com sucesso!")
        print(f"Próximo ID disponível: {CUSTOMERS_ID}")
        
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {json_path}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o arquivo JSON: {str(e)}")
    except Exception as e:
        print(f"Erro inesperado ao carregar clientes: {str(e)}")