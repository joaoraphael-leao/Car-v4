import os
import classes
import car_management

user_input = ''
reg_car = {}
maintenance_record = {}
service_record = {}
damage_record = {}
incident_record = {}

def car_reports_management_main():

    global user_input
    
    while user_input != '5':

        menu = classes.Car_Reports_Management_Menu()
        menu.show_menu()
        menu.interact_menu()

        user_input = input('\n')
        os.system('cls')

        # Maintenance Menu
        if user_input == '1':
            
            # Add new maintenance report
            # Preciso implementar as classes especificas com polimorfismo
            # Talvez fazer uma so lista com tudo?
            while user_input != '3':

                menu.maintenance_submenu_header()
                menu.maintenance_submenu()

                user_input = input('\n')
                os.system('cls')

                if user_input == '1':
                    print("Add a new Maintenance report\n\n")
                    
                    car_id = input("Insert the ID of the Car\n")
                    date = input("Insert the date of the Maintenance\n")
                    details = input("Insert the details of the Maintenance\n")
                    # ate aqui mantem

                    #substituir
                    reg_car['Date'] = date
                    reg_car['Details'] = details

                    # isso mantem
                    car_management.car_list[car_id].maintenance_details = details
                    car_management.car_list[car_id].maintenance_date = date

                    maintenance_record['aux'] = reg_car

                    maintenance_record[car_id] = maintenance_record['aux']
                    del maintenance_record['aux']
                

                    os.system("cls")
                    print("New Maintenance entry added!\n")
                    

car_reports_management_main()
                

