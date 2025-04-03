import os
import classes

customers_list = []

user_input = ''

def customer_main():

    global user_input

    while user_input != '3':

        menu = classes.Customer_Menu()
        menu.show_menu()
        menu.interact_menu()

        user_input = input("\n")
    
        if user_input == '1':

            os.system('cls')

            name = input("Insert a name\n")
            id = input("Insert a ID\n")
            nickname = input("Insert a nickname\n")

            customer = classes.Customer(nickname, 
                                        id, 
                                        name,
                                        "0", "0","No Data", "No Data")
            
            customers_list.append(customer)

            os.system("cls")

            print("Profile Created!\n")
        
        elif user_input == '2':
            os.system('cls')
            print("Customer List\n")
            for i in range(len(customers_list)):
                print(customers_list[i])
    os.system('cls')
        