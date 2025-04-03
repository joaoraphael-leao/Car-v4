import os
import classes
import car_management
import car_request
import car_customer_list

user_input = ''
deposit_value = ''
bank = ''
refund_requests = {}

def main_payment_processing():

    global user_input
    global deposit_value
    global bank

    while user_input != '4':

        menu = classes.Payment_Processing_Menu()
        menu.show_menu()
        menu.interact_menu()

        if user_input == '1':

            os.system('cls')

            print("Payment Menu\n\n")

            car_payment_id = input("Insert the ID of the car\n")

            user_nickname = input("Insert the user Nickname\n")

            print(f"Total owed by {user_nickname}: {car_management.car_list[car_payment_id].price_day} \n")

            value_owned = car_management.car_list[car_payment_id].price_day

            car_customer_list.customers_list[0].debt += value_owned

            user_input = input('Procceed to payment page? (Yes or No)\n')
            if user_input.lower() == 'yes' : break
        
        elif user_input == '2':

            os.system('cls')

            print("Deposit Menu\n\n")

            deposit_choice = input("1. Make a Deposit\n2. See Deposits\n")

            if deposit_choice == '1':

                user_input = input("Insert the account Nickname you want to make a deposit\n")


                value_deposit = input("Insert the value you want to deposit\n")

                car_customer_list.customers_list[0].funds += value_deposit

                bank[user_input] = value_deposit

                print(f"Deposited R$ {value_deposit} on {user_input} Account")
            
            elif deposit_choice == '2':
                os.system('cls')
                print(bank)
        
        elif user_input == '3':

            os.system('cls')
        
            print("Refund Menu\n\n")

            user_input = input(f"Select the request you want to apply for a Refund\n {car_request.requests}\n")

            refund_requests[user_input] = input("Insert the reason you want to make a Refund.\n")  

    os.system('cls')        
