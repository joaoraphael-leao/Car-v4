import os
import classes
import car_management

user_input = ''
cars_discounts = {}
cars_special_offers = {}
modification_discount = {}
modification_special_offers = {}

def main_car_pricing_and_offers():

    global user_input

    while user_input != '4':

        menu = classes.Car_Pricing_And_Offers_Menu()
        menu.show_menu()
        menu.interact_menu()

        user_input = ('\n')
        os.system('cls')

        if user_input == '1':

            print("Pricing and Special Offers Menu\n\n")
            user_input = input("1. Manage Pricing\n2. Manage Discounts\n3. Manage Special Offers\n4. Exit\n")

            if user_input.lower() == '1':

                os.system('cls')
                print("Price Management Menu\n\n")
            
                user_input = input(f"Insert the ID of the car you want to change the price\n{car_management.car_list}\n\n")
                new_value = input("Insert the new price of the car\n")

                car_management.car_list[user_input].price_day = new_value

                os.system('cls')
                print("Car price changed!\n")

            elif user_input.lower() == '2' :
            
                os.system('cls')
                print("Discounts Management Menu\n\n")

                car_id = input(f"Insert the ID of the car you want to add a Discount\n{car_management.car_list}\n")
                new_value = input("Insert the new price of the car with the Discount\n")
                remaining_duration = input("Insert the remaining duration of the Discount\n")

                modification_discount['Discounted Value'] = new_value
                modification_discount['Remaining Duration'] = remaining_duration

                car_management.car_list[car_id].offer = f"This car has a discount, the current price is: {new_value}"

                cars_discounts['aux'] = modification_discount
                cars_discounts[car_id] = cars_discounts['aux']
                del cars_discounts['aux']

                os.system('cls')
                print("Discount added to the list!\n")
            
            elif user_input.lower() == '3':

                os.system('cls')
                print("Special Offers Management Menu\n\n")

                Car_ID = input(f"Insert the ID of the car you want to add a Special Offer\n{car_management.car_list}\n")
                New_Value = input("Insert the new price of the car\n")
                Remaining_Duration = input("Insert the remaining duration of the Special Offer\n")
                Special_Condition = input("Insert the Special Condition for the Special Offer\n")

                modification_special_offers['Special Value'] = New_Value
                modification_special_offers['Remaining Duration'] = Remaining_Duration

                car_management.car_list[Car_ID].offer = f"This car has a Special Offer:\nSpecial Price:{New_Value}\nCondition:{Special_Condition}"

                cars_special_offers['aux'] = modification_special_offers
                cars_special_offers[Car_ID] = cars_special_offers['aux']
                del cars_special_offers['aux']

                os.system('cls')
                print("Special Offer added to the list!\n")
        elif user_input.lower() == '2':

            print("What would you like to see?\n\n")

            user_input = input("1. Discounts\n2. Special Offers\n")

            if user_input.lower() == '1' :

                os.system('cls')
                print(cars_discounts)

            elif user_input.lower() == '2':
            
                os.system('cls')
                print(cars_special_offers)
    os.system('cls')
main_car_pricing_and_offers()