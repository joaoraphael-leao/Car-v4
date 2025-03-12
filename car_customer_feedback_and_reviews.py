import os
import classes
import car_customer_list

user_input = ''
user_feedbacks = []
new_feedback = {}

def main_car_customer_feedback_and_reviews():

    global user_input,user_feedbacks,new_feedback

    while user_input != '3':

        menu = classes.Car_Customer_Feedback_And_Reviews_Menu()
        menu.show_menu()
        menu.interact_menu()

        if user_input.lower() == '1':
        
            print("Feedback and Review Submit Menu\n\n")

            new_feedback['Nickname'] = input("Insert your nickname\n")
            new_feedback['Date'] = input("Insert the date you are writing this feedback\n")
            new_feedback['Car ID'] = input("Insert the Car ID form the car you rented\n")
            new_feedback['Feedback'] = input("Insert your Feedback\n")

            car_customer_list.customers_list[0].reviews = f"{new_feedback['Date']}: Rented {new_feedback['Car ID']}\nFeedback: {new_feedback['Feedback']}"

            user_feedbacks.append(new_feedback)
            os.system('cls')
            print("Feedback and Review Submitted!")
        
        elif user_input.lower() == '2':
            os.system('cls')
            print(user_feedbacks)

    os.system('cls')

main_car_customer_feedback_and_reviews()

