import classes
import os
from car_management import main_car_management
from car_customer_list import customer_main
from car_request import car_request_main
from car_reports_management import car_reports_management_main
from car_payment_processing import main_payment_processing
from car_rental_agreement import main_car_rental_agreement
from car_pricing_and_offers import main_car_pricing_and_offers
from gps_tracking import gps_tracking_main

while True:
    
    main_menu = classes.Menu_Selector()
    main_menu.show_menu()
    main_menu.interact_menu()

    user_input = input("\n")
    os.system('cls')

    if user_input == "1":
        main_car_management()
    elif user_input == "2":
        customer_main()
    elif user_input == "3":
        car_request_main()
    elif user_input == "4":
        car_reports_management_main()
    elif user_input == "5":
        main_payment_processing()
    elif user_input == "6":
        main_car_rental_agreement()
    elif user_input == "7":
        main_car_pricing_and_offers()
    elif user_input == "8":  
        gps_tracking_main()
    elif user_input.lower() == "sair":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")