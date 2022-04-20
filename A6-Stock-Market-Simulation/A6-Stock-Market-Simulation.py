##################################################
## Assignment 6: STOCK MARKET SIMULATION
## Author: Jordan Chen
## Email: jordanchen50@gmail.com
## Class: MIS-515 Spring 2021
##################################################

# This program simulates a random walk stock market, meaning stock prices randomly increase or decrease each day
import random, csv

# Start of functions
def randwalk(initial_price, simulation):

  ''' This function runs to simulate a random market'''

  # Counter start for days that can increase/decrease/stay the same 
  increased = 0
  decreased = 0
  same = 0

  # Allows program to update price day by day while also printing intial price at the end
  changed_price = initial_price

  # Starts a loop for user input simulation number 
  for i in range(1, simulation + 1, 1):
    # Generates random number from -3 to 3
    change = random.randint(-3,3)
    # Math to update price with random number 
    changed_price = changed_price * (1 + (change/100))

    # Updates increase/decrease/same counter by 1 each loop
    if change < 0:
      decreased += 1
    elif change == 0:
      same += 1
    elif change > 0:
      increased += 1

  # Appends final numbers into randwalk.csv
  with open("/content/drive/MyDrive/MIS 515/randwalk.csv","a") as file:
    writer = csv.writer(file, lineterminator = "\n")
    new_row = [initial_price, simulation, changed_price, increased, decreased]
    writer.writerow(new_row)

  # Prints out simulation numbers to user
  print("After", simulation, "days,", changed_price, "is the new stock price. The stock price increased", increased, "time(s), decreased",decreased,"time(s), and stayed the same", same, "time(s).")
##### END OF FUNCTION

# Allows user to run as many simulations as they'd like
repeat = "yes"
while repeat.lower() == "yes":

  # Asks user input initial price and simulation length
  initial_price = float(input("What is the initial price of the stock? "))
  simulation = int(input("How many days would you like to simulate? "))

  # Tests to see if randwalk.csv exists. If it does, it moves straight to randwalk function
  # Try/Except block allows user to append data even if randwalk.csv already exists without disturbing previous data entered 
  try:
    with open("/content/drive/MyDrive/MIS 515/randwalk.csv","r") as test:
      reader = csv.reader(test)

    randwalk(initial_price, simulation)
    
    repeat = input("Would you like to perform another simulation (yes/no)? ")

  # Moves to except block if randwalk.csv does not exist. This will write a new csv file and create the header row
  except:
    with open("/content/drive/MyDrive/MIS 515/randwalk.csv","w") as file:
      writer = csv.writer(file, lineterminator = "\n")
      header_row = ["Initial Price:", "Days:", "Final Price:","Price Increased:", "Price Decreased"]
      writer.writerow(header_row)

    randwalk(initial_price, simulation)

    repeat = input("Would you like to perform another simulation (yes/no)? ")