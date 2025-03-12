import classes
import os
from car_management import main_car_management

while True:
    
    main_menu = classes.Menu_Selector()
    main_menu.show_menu()
    main_menu.interact_menu()

    user_input = input("\n")

    if user_input == "1" :
        main_car_management()