from src.controllers.global_dicts import customers, CUSTOMERS_ID
from src.models.customer import CustomerBuilder

def add_customer():
    global CUSTOMERS_ID
    email = input("Enter email: ")
    if customers.get(email):
        print("A Customer with this email already exists.")
        return

    Customer = CustomerBuilder()
    Customer.com_email(email)

    name = input("Enter name: ")
    Customer.com_name(name)
    Customer.com_wallet(0)

    password = input("Enter password: ")
    Customer.com_password(password)
    Customer.com_id(CUSTOMERS_ID)
    try:
        Customer_final = Customer.build()
        CUSTOMERS_ID += 1
        customers[email] = Customer_final
        print("Customer added successfully.")
    except ValueError as e:
        print(e)
        return None
    return 

# login
def login():
    email = input("Enter email: ")
    customer = find_customer(email)
    if not customer:
        print("Customer not found.")
        return None
    password = input("Enter password: ")
    if customer.password != password:
        print(customer.password, " ", password)
        print("Incorrect password.")
        return None
    print("Login successful.")
    return customer 

def show_customers():
    if not customers:
        print("No customers found.")
        return

    for email, customer in customers.items():
        print(f"Email: {email}, Name: {customer.com_name}, Wallet: {customer.com_wallet}")

def find_customer(email):
    customer = customers.get(email)
    if customer:
        print(f"Customer found: {customer.name}")
        return customer
    else:
        print("Customer not found.")

def update_customer():
    customer = login()
    if not customer:
        return "Try again"
    print("1. Update name")
    print("2. Update password")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        new_name = input("Enter new name: ")
        customer.name == new_name
        print("Name updated successfully.")
    elif choice == '2':
        amount = float(input("Enter amount to add: "))
        customer.wallet_add(amount)
        print("Funds added successfully.")
    else:
        print("Invalid choice.")
    


##delete_customer
def delete_customer(email):
    customer = find_customer(email)
    if not customer:
        print("Customer not found.")
        return
    authenticated = login()
    if authenticated == customer:
        del customers[email]
        print("Customer deleted successfully.")
