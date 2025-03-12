import os
import classes
import car_management

user_input = '' 
user_input_maintenance = ''
user_input_service = ''
user_input_damage = ''
user_input_incident = ''
records = []

def car_reports_management_main():

    global user_input, user_input_maintenance, user_input_service, user_input_damage, user_input_incident
    
    while user_input != '6':

        menu = classes.Car_Reports_Management_Menu()
        menu.show_menu()
        menu.interact_menu()

        user_input = input('\n')
        os.system('cls')

        # Maintenance Menu
        if user_input == '1':
            
            # Add new maintenance report
            while user_input_maintenance != '2':

                menu.maintenance_submenu_header()
                menu.maintenance_submenu()

                user_input_maintenance = input('\n')
                os.system('cls')

                if user_input_maintenance == '1':
                    print("Add a new Maintenance report\n\n")
                    
                    car_id = input("Insert the ID of the Car\n")
                    date = input("Insert the date of the Maintenance\n")
                    details = input("Insert the details of the Maintenance\n")
                    
                    maintenance_aux = classes.Maintenance(car_id, date, details)

                    car_management.car_list[car_id].maintenance_details = details
                    car_management.car_list[car_id].maintenance_date = date

                    records.append(maintenance_aux)

                    os.system("cls")
                    print("New Maintenance entry added!\n")

        # Service Menu
        if user_input == '2':
            
            # Add new service report
            while user_input_service != '2':

                menu.service_submenu_header()
                menu.service_submenu()

                user_input_service = input('\n')
                os.system('cls')

                if user_input_service == '1':
                    print("Add a new Service report\n\n")
                    
                    car_id = input("Insert the ID of the Car\n")
                    date = input("Insert the date of the Service\n")
                    details = input("Insert the details of the Service\n")
                    
                    service_aux = classes.Service(car_id, date, details)

                    car_management.car_list[car_id].service_details = details
                    car_management.car_list[car_id].service_date = date

                    records.append(service_aux)

                    os.system("cls")
                    print("New Service entry added!\n")

        # Damage Menu
        if user_input == '3':
            
            # Add new damage report
            while user_input_damage != '2':

                menu.damage_submenu_header()
                menu.damage_submenu()

                user_input_damage = input('\n')
                os.system('cls')

                if user_input_damage == '1':
                    print("Add a new Damage report\n\n")
                    
                    car_id = input("Insert the ID of the Car\n")
                    date = input("Insert the date of the Damage\n")
                    details = input("Insert the details of the Damage\n")
                    
                    damage_aux = classes.Damage(car_id, date, details)

                    car_management.car_list[car_id].damage_details = details
                    car_management.car_list[car_id].damage_date = date

                    records.append(damage_aux)

                    os.system("cls")
                    print("New Damage entry added!\n")

        # Incident Menu
        if user_input == '4':
            
            # Add new incident report
            while user_input_incident != '2':

                menu.incident_submenu_header()
                menu.incident_submenu()

                user_input_incident = input('\n')
                os.system('cls')

                if user_input_incident == '1':
                    print("Add a new Incident report\n\n")
                    
                    car_id = input("Insert the ID of the Car\n")
                    date = input("Insert the date of the Incident\n")
                    details = input("Insert the details of the Incident\n")
                    
                    incident_aux = classes.Incident(car_id, date, details)

                    car_management.car_list[car_id].incident_details = details
                    car_management.car_list[car_id].incident_date = date

                    records.append(incident_aux)

                    os.system("cls")
                    print("New Incident entry added!\n")

        # See Reports
        elif user_input == '5':
            
            os.system('cls')
            menu.record_history_header()
            for i in range(len(records)):
                print(records[i])                    

car_reports_management_main()
                

