##################################################
## Assignment 3: SIMULATION EXPERIMENTS
## Author: Jordan Chen
## Email: jordanchen50@gmail.com
## Class: MIS-315 Fall 2020
##################################################

import random

print("Welcome to the Weather Simulator!\n")

# Different string conditions for simulation to stop 
parameter_1 = "0,0,0,0,0,0,0,0,0,0,0,0,0,0"
parameter_2 = "1,3"
parameter_3 = "3,1"
parameter_4 = "1,1"
parameter_5 = "3,3"

# Start of user input while loop 
repeat = "yes"

while repeat.lower() == "yes":
    
    rainfall = []
    sim_stop = "no"
    
    while sim_stop == "no":
          
        # Random number generator 
        psuedo_random = random.randint(1,100)
            
        # Heavy Rain 
        if psuedo_random >= 1 and psuedo_random <= 5:
            rainfall.append(3)
            print("Heavy Rain Today! 3 Inches Fell.")
                
        # Light Rain 
        elif psuedo_random > 5 and psuedo_random <= 15:
            rainfall.append(1)
            print("Light Rain Today! 1 Inch Fell.")
                    
        # No Rain
        else:
            print("No Rain Today...")
            rainfall.append(0)
        
        # Converts rainfall list into string to do parameter serachers later on 
        converted_rainfall = [str(i) for i in rainfall]
        joined_rainfall = ",".join(converted_rainfall)
        
        # Searches for greater than or equal to 8 inches of rain fall 
        sum_rainfall = sum(rainfall)
        
        # Parameters to stop simulation
        # No rain for 14 days
        if parameter_1 in joined_rainfall:
            sim_stop = "yes"
            print("\n14 consecutive days of no rain. It looks like a drought. Think about planning crops elsewhere.")
        
        # 2 straight days of rain and >8 inches of rainfall
        elif parameter_2 in joined_rainfall and sum_rainfall >=8:
            sim_stop = "yes"
            print("\n2 conescutive days of rain! The rainy season is starting and total rainfall has also reached at least 8 inches. The soil is moist enought to plant!")
            
        elif parameter_3 in joined_rainfall and sum_rainfall >=8:
            sim_stop = "yes"
            print("\n2 conescutive days of rain! The rainy season is starting and total rainfall has also reached at least 8 inches. The soil is moist enought to plant!")
            
        elif parameter_4 in joined_rainfall and sum_rainfall >=8:
            sim_stop = "yes"
            print("\n2 conescutive days of rain! The rainy season is starting and total rainfall has also reached at least 8 inches. The soil is moist enought to plant!")
            
        elif parameter_5 in joined_rainfall and sum_rainfall >=8:
            sim_stop = "yes"
            print("\n2 conescutive days of rain! The rainy season is starting and total rainfall has also reached at least 8 inches. The soil is moist enought to plant!")
            
        # Only 2 straight days of rainfall 
        elif parameter_2 in joined_rainfall or parameter_3 in joined_rainfall or parameter_4 in joined_rainfall or parameter_5 in joined_rainfall:
            sim_stop = "yes"
            print("\n2 conescutive days of rain! The rainy season is starting so it must be time to plant!")
        
        # >8 inches of rainfall 
        elif sum_rainfall >=8:
            sim_stop = "yes"
            print("\nTotal rainfall has reached at least 8 inches. The soil is moist enought to plant!")

    try:
        repeat = input("\nWould you like to run another simulation (yes/no)? ")
        print(" ")

    except Exception as e:
        print("An unexpected error has occured.")
        print(e)

print("Thank you for using the Weather Simulator!")
