#!/usr/bin/env python3
# Created by: Alex M
# Created on: Nov 14, 2023
# This program gets user_password and if its right they can go through


def main():
    #initializing counter to 0 and displaying intro statement 
    loop_counter = 0
    print("Hello Passenger!!. To open this door you have to enter a 6 digits pin code !!!")
    while True:
        #getting user password 
        user_password_str = input("")
        #using try catch to catch any string 
        try:
            user_password = int(user_password_str)
        except ValueError :

            print(f"{user_password_str} is not a valid input try again or enter 5 to quit ")
            

        else:
            #checking for negative inputs, if true display invalid  
            if user_password < 0:
                print(f"{user_password} is not a valid input try again or enter 5 to quit ")
                
            else:
                #initializing the correct password 
                correct_password = 159236
                #checking if password is correct then breaking the loop 
                if user_password == correct_password:
                    print(" correct password, you can pass ")
                    break
                #breaking the loop if user enters 5 
                elif user_password == 5 :
                        print ("thank you for playing ")
                        break
                #checking if password is incorrect and displaying the result
                elif user_password != correct_password :
                    print (" incorrect password, try again or enter 5 to quit ")
                    loop_counter = loop_counter +1
                    
                    
                    #if the user gets the password wrong 6 times giving a hint
                    if loop_counter == 6 :
                        print(" Hint!!! The password is joe's password ")
                    
                    else:
                        print()
                else:
                    print()
        
            





if __name__ == "__main__":
    main()