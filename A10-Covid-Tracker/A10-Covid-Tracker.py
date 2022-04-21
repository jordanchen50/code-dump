##################################################
## Assignment 10: COVID TRACKER
## Author: Jordan Chen
## Email: jordanchen50@gmail.com
## Class: MIS-515 Spring 2021
##################################################

# This program will allow users to pull up data on COVID 19 statistics in the United States
import json, requests, sys
import matplotlib.pyplot as plt
response = requests.get('https://api.covidtracking.com/v1/states/daily.json')

# Testing to see if a connection issue occurs
if response.status_code == 200:
  data = json.loads(response.text.lower())
else:
  print("Sorry, an error has occurred with connecting to the API. Please contact developer to fix and try again later.")
  sys.exit()

# Creating a large list of all values to validate user inputs
meta_data = []
for line in data:
  temp_list1 = list(line.values())
  temp_list2 = list(line.keys())
  for item in temp_list1:
    meta_data.append(item)
  for item in temp_list2:
    meta_data.append(item)

# Getting the most recent date in the API
for line in data:
  most_recent_date = line['date']
  break

# Start of user entered criteria
print("Welcome to the coronavirus (COVID-19) live data analyzer!\n")

repeat = 'yes'
while repeat == 'yes':
  user_location = input('Which location would you like to search? ').lower()

  # Testing if location user entered is valid
  if user_location in meta_data:

    user_statistic = input('\nWhich statistic would you like to search? ').lower()
    
    print('\nDisclaimer: This program is limited to a max of 4 months (About 120 Days) for readability sake. Please keep this in mind when choosing a start/end date.')

    # Testing if statistic user requested is valid
    if user_statistic in meta_data:

      user_start_request = input('\nWould you like to add a start data (yes/no)? ').lower()

      if user_start_request == 'yes':
        user_start = int(input('Which start date would you like to use (YYYMMDD)? '))
        
        if user_start < 20200113:
          print("Sorry, the date you entered is before the first COVID case was recorded. Start date will be set to January 13th, 2020.")
          user_start = 20200113

      elif user_start_request == 'no':
        # Default start date is the earliest date recorded in the dataset 
        user_start = 20200113

      else:
        print("Sorry an error has occurred. Please try again and enter yes or no for the previous question")
        break

      user_end_request = input('\nWould you like to add an end data (yes/no)? ').lower()
        
      if user_end_request == 'yes':
        user_end = int(input('Which end date would you like to use (YYYMMDD)? '))

        if user_end > most_recent_date:
          print("Sorry, the date you entered is further than the API's most recent date. The end date will be set to the most recent date.")
          user_end = most_recent_date

      elif user_end_request == 'no':
        # Default end date is the most recent date recorded in the dataset
        user_end = most_recent_date

      else:
        print("Sorry an error has occurred. Please try again and enter yes or no for the previous question")
        break

      x_axis = []
      y_axis = []
      dates = []
      print_data = []

      # Counter is used to format the x axis correctly. The dates had large gaps between months and years so counter is used to make x axis uniform.
      counter = 0
      month_counter = 0

      header = "Coronavirus in " + user_location.upper() + " between " + str(user_start) + " and " + str(user_end) + ": " + str(user_statistic)

      print("\n" + header)
      print("\nDate     ", user_statistic)

      for line in data:

        date = int(line['date'])

        # Only accepts data that fits user entered criteria 
        if line['state'] == user_location and date >= user_start and date <= user_end:
          statistic = line[user_statistic]

          if month_counter < 120:

            # Data has null, this if statements turns null into 0 so data is graphable
            if statistic == "null":
              statistic = 0
            
            counter += 1
            month_counter += 1

            temp = [date, statistic]
            print_data.append(temp)

            x_axis.append(counter)
            y_axis.append(statistic)
            dates.append(date)

      # Necessary to reverse the data and print it out chronologically
      y_axis.reverse()
      dates.reverse()
      print_data.reverse()
      for date, statistic in print_data:
        print(date, "    ", statistic)

      # Plotting the graph
      f = plt.figure()
      f.set_figwidth(10)
      f.set_figheight(5)
      plt.bar(x_axis, y_axis)
      plt.xticks(rotation = 90, ha = "right")
      plt.xticks(x_axis, dates)
      plt.title(header)
      plt.xlabel('Date')
      plt.ylabel(user_statistic)
      plt.show()

    else:
      print("Sorry, the statistic you requested is not in the dataset. Please try again.")
  else:
    print("Sorry, the state you requested is not in the dataset. Please try again.")

  repeat = input('\nPerform another analysis (yes/no)? ').lower()

print("\nThank you for using the coronavirus (COVID-19) live data analyzer!")