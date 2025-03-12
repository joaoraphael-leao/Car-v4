import classes
import os

car_list = {}
user_input = ''

def main_car_management():

    global user_input

    while user_input.lower() != '3' :

        menu = classes.Management_Menu()
        menu.show_menu()
        menu.interact_menu()

        user_input = input("\n")

        if user_input.lower() == '1':
        
            brand = input("Insert the car Brand\n")
            model = input("Insert the car Model\n")
            color = input("Insert the car Color\n")
            horse_power = input("Insert the car HP(Horse Power)\n")
            price_day = input("Insert the Rental Price\n")
            available = input("Insert if the car is Available or not (Yes or No)\n")
        
            new_car = classes.Vehicle(brand, model, color, horse_power, price_day, available, 
                                      "", "No Data",
                                        "", "No Data",
                                            "", "No Data",
                                              "", "No Data",
                                                "No Offers for this vehicle")

            car_list['aux'] = new_car

            car_id = input("Set an ID for the car\n")
            car_list[car_id] = car_list['aux']
            del car_list['aux']

            os.system('cls')
            print("The car was added to the car List\n")


        elif user_input.lower() == '2':
            os.system('cls')
            print("Car list\n")
            [print(f"ID: {key}\n\n{value}\n\n") for key, value in car_list.items()]
            print("\n")

    os.system('cls')


main_car_management()