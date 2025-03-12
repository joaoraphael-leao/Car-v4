import os
import classes
import car_management
import car_customer_list


requests = {}
user_input = ''

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

                user_input = input("Insert your Nickname\n")

                requests[car_request_id] = user_input

                car_management.car_list[car_request_id].available = 'No'
                car_customer_list.customers_list[0].last_rent = car_request_id #
                os.system('cls')
                print("Car successfully requested!\n")
            
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
            
            elif car_management.car_list[car_request_id].available.lower() == 'yes':
                os.system('cls')
                print("There is no request for this car!\n")
car_request_main() 