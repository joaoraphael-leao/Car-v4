from src.controllers.global_dicts import customers

def add_funds(email, amount):
    try:
        customer = customers.get(email)
        if not customer:
            print("Customer not found.")
            return False
        customer.wallet_add(float(amount))
        print(f"Funds added successfully. New balance: R${customer.wallet:.2f}")
        return True
    except ValueError as e:
        print(f"Error adding funds: {e}")
        return False

def check_balance(email):
    customer = customers.get(email)
    if not customer:
        print("Customer not found.")
        return None
    print(f"Wallet {customer.wallet}") 

def pay_debts(email):
    try:
        customer = customers.get(email)
        if not customer:
            print("Customer not found.")
            return False
        if not customer.has_debts():
            print("There are no pending debts.")
            return True
            
        debts = customer.get_debts()
        if customer.wallet >= debts:
            customer.wallet_subtract(debts)
            customer.clear_debts()
            print(f"Debts of ${debts:.2f} paid successfully. New balance: ${customer.wallet:.2f}")
            return True
        else:
            print(f"Insufficient balance. Debts: ${debts:.2f}, Balance: ${customer.wallet:.2f}")
            return False
    except Exception as e:
        print(f"Error paying debts: {e}")
        return False