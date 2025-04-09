from src.controllers.global_dicts import cars, special_offers
from src.controllers.car_controller import show_cars

def update_car_price():
    """Update base price of a car"""
    show_cars()
    car_id = input("Digite o ID do carro para alterar o preço: ")
    
    if car_id not in cars:
        print("Carro não encontrado")
        return
        
    try:
        new_price = float(input("Digite o novo preço base: "))
        cars[car_id].daily_rate = new_price
        print("Preço atualizado com sucesso!")
    except ValueError:
        print("Preço inválido")

def add_special_offer():
    """Add special offer to a car"""
    show_cars()
    car_id = input("Digite o ID do carro para adicionar oferta especial: ")
    
    if car_id not in cars:
        print("Carro não encontrado")
        return
        
    try:
        special_price = float(input("Digite o preço especial: "))
        duration = input("Digite a duração da oferta (dias): ")
        conditions = input("Digite as condições da oferta: ")
        
        offer = {
            'special_price': special_price,
            'duration': duration,
            'conditions': conditions
        }
        
        special_offers[car_id] = offer
        cars[car_id].offer = f"Oferta Especial: R${special_price}\nCondições: {conditions}"
        print("Oferta especial adicionada com sucesso!")
        
    except ValueError as e:
        print(f"Erro ao adicionar oferta especial: {e}")

def show_special_offers():
    """Show all active special offers"""
    if not special_offers:
        print("\nNenhuma oferta especial ativa")
        return
        
    print("\n=== Ofertas Especiais Ativas ===")
    for car_id, offer in special_offers.items():
        print(f"\nCarro ID: {car_id}")
        print(f"Preço Especial: R${offer['special_price']}")
        print(f"Duração: {offer['duration']} dias")
        print(f"Condições: {offer['conditions']}")
        print("===========================")