import os
import classes


agreements_list = {}
user_input = ''
user_1 = ''
user_2 = ''

def main_car_rental_agreement():

    global user_input, user_1, user_2

    while user_input != '4':

        menu = classes.Car_Rental_Agreement_Menu()
        menu.show_menu()
        menu.interact_menu()

        if user_input == '1':
            
            os.system('cls')
            print("New Agreement Menu\n\n")

            user1 = input("Insert your nickname\n")
            user2 = input("Insert the nickname of who you want to make an agreement\n")
            car_id = input("Insert the ID of the car you want to make an agreement\n")

            agreements_list[car_id]['Buyer'] = user1
            agreements_list[car_id]['Owner'] = user2

            os.system('cls')
            print("Agreement created!\n")
        
        elif user_input.lower() == '2' :

            os.system('cls')
            print("Cancel Agreement Menu")

            car_id = input("Insert the ID of the car you want to cancel the agreement\n")

            agreements_list.pop(car_id)

            os.system("cls")
            print("Car Agreement Canceled!\n")
        
        elif user_input.lower() == '3' :
        
            os.system('cls')
            print("Agreements List\n")
            print(agreements_list)
main_car_rental_agreement()
            
