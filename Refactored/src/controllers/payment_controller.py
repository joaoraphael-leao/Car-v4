from src.controllers.global_dicts import customers

def add_funds(email, amount):
    try:
        customer = customers.get(email)
        if not customer:
            print("Cliente não encontrado.")
            return False
        customer.wallet_add(float(amount))
        print(f"Saldo adicionado com sucesso. Novo saldo: R${customer.wallet:.2f}")
        return True
    except ValueError as e:
        print(f"Erro ao adicionar fundos: {e}")
        return False

def check_balance(email):
    customer = customers.get(email)
    if not customer:
        print("Cliente não encontrado.")
        return None
    print(f"Wallet {customer.wallet}") 

def pay_debts(email):
    try:
        customer = customers.get(email)
        if not customer:
            print("Cliente não encontrado.")
            return False
        if not customer.has_debts():
            print("Não há débitos pendentes.")
            return True
            
        debts = customer.get_debts()
        if customer.wallet >= debts:
            customer.wallet_subtract(debts)
            customer.clear_debts()
            print(f"Débitos de R${debts:.2f} pagos com sucesso. Novo saldo: R${customer.wallet:.2f}")
            return True
        else:
            print(f"Saldo insuficiente. Débitos: R${debts:.2f}, Saldo: R${customer.wallet:.2f}")
            return False
    except Exception as e:
        print(f"Erro ao pagar débitos: {e}")
        return False