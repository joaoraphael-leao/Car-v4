import json 
import os
from src.models.customer import CustomerBuilder
from src.controllers.global_dicts import customers, CUSTOMERS_ID

def load_customers():
    """
    Loads customer data from JSON file and updates the global counter
    """
    global CUSTOMERS_ID
    
    json_path = os.path.join("src", "data", "customers.json")
    
    try:
        with open(json_path, "r", encoding='utf-8') as file:
            data = json.load(file)
            
        if not isinstance(data, list):
            raise ValueError("The JSON file must contain a list of customers")
            
        for customer_data in data:
            # Validação dos campos obrigatórios
            required_fields = ["email", "name", "wallet", "password"]
            if not all(field in customer_data for field in required_fields):
                print(f"Warning: Customer with incomplete data ignored: {customer_data}")
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
                print(f"Error creating customer {customer_data.get('name', 'unknown')}: {str(e)}")
                continue
                
        print(f"Successfully loaded {len(customers)} customers!")
        print(f"Next available ID: {CUSTOMERS_ID}")
        
    except FileNotFoundError:
        print(f"File not found: {json_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file: {str(e)}")
    except Exception as e:
        print(f"Unexpected error loading customers: {str(e)}")