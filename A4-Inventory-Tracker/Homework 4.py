##################################################
## Assignment 4: INVENTORY TRACKER
## Author: Jordan Chen
## Email: jordanchen50@gmail.com
## Class: MIS-315 Fall 2020
##################################################

# This code takes pre existing .csv files and complies/analyzes them
import csv

# Starts user controlled while loop
repeat = "yes"
total = 0

# Lists used for future analysis 
inventory_records = []
shelf_space = []

print("Welcome to the inventory tracker!")

while repeat.lower() == "yes":
    
    mode = input("\nWhat would you like to perform (import/statistics)? ")
    
    # Import function of the inventory tracker
    if mode.lower() == "import":
        
        csv_file = input("Which file would you like to import? ")
        
        try:
            
            # Creates new .csv file for compiled data
            with open("inventory_records_out.csv","a") as file_records:
                writer = csv.writer(file_records, lineterminator = "\n")
                
                # Reads user imputed .csv files
                with open(csv_file,"r") as file:
                    reader = csv.reader(file)
                    
                    total_for = 0
                    
                    for line in reader:
                        
                        identification = line[0]
                        qunatity = line[2]
                        size = line[4]
                        total_space = float(qunatity) * float(size)
                        
                        # Checker for duplications 
                        if identification in inventory_records:
                            print("Data for ID",identification,"is already in the inventory records.")
                        else:
                            writer.writerow(line)
                            inventory_records.append(identification)
                            shelf_space.append(total_space)
                            total_for = total_for + 1 
        
                total = len(inventory_records)
                
                print(total_for,"total inventory records sucessfully loaded.")
                
        # Catch all for errors like unrecognized files 
        except:
            print("Sorry, that file could not be found. Please try again.")
            
    # If user tries do statistic function but there is no imported data 
    elif mode.lower() == "statistics" and len(inventory_records) == 0:
        print("Sorry, no inventory data was loaded yet. Please try again.")
    
    # Stastitics function 
    else:
        print("Types of inventory:",total)
        print("Total shelf space:", sum(shelf_space))
    
    repeat = input("\nWould you like to run any further analyses (yes/no)? ")
    
print("\nThank you for using the inventory tracker!")