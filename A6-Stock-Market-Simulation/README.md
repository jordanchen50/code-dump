# MIS 515 ASSIGNMENT 6:

# STOCK MARKET SIMULATION

Completed Febuary 26th, 2021 (2/26/2021)

Your assignment is to create a Python program that performs a “random walk” stock market
simulation. The random walk hypothesis argues that the stock prices randomly increase or
decrease each day relative to their prices the previous day, and these changes in price cannot be
predicted.

To perform the simulation, first ask the user for:

1. the initial price of the stock
2. How many days they would like to simulate

Then, each day, assume that the change in stock price will be random and range from a 3 percent
increase to a 3 percent decrease relative to the previous day. Ensure that your program captures
the daily change in stock price. In addition, also keep track of how many days the stock price
increased, how many days the stock price decreased, and how many days the stock price stayed
the same. At the end of the simulation, report (print) the new stock price and the number of days
that the stock price increased, decreased, and stayed the same.

Each time you make an adjustment to the stock price, ensure that the new price reflects an
appropriate percentage change relative to the previous day. For example, suppose that your stock
has an initial price of $10.00. If the stock price increases by 3 percent the first day, the new stock
price is calculated as $10.00 x 1.0 3 = $10. 3. If the stock price decreases by 3 percent the second
day, then the new stock price is calculated as $10. 3 x 0.9 7 = $9.99 1. In other words, ensure that
the change in stock price each day is calculated based on the stock price from the previous day.

Once a simulation is complete, the program should ask the user if they would like to run the
simulation again and allow the user to run the simulation an unlimited number of times.

Your program should:

1. Write the results of the simulation to an output CSV file called randwalk.csv. Create a
    “header row” at the top of your CSV file to title each column (“Initial price”, “Days”
    refers to the Number of days simulated, “Final price”, “Price increased” refers to Number
    of days price increased, and “Price decreased” refers to the Number of days price
    decreased.
2. Each time a simulation is run, create a new row in your CSV file containing the initial
    price, number of days simulated, final price, Number of days price increased, and
    Number of days price decreased for that simulation.

Some considerations to note:

- Feel free to import an appropriate module
- You may assume that the user indicates both the initial stock price and the number of
    days to simulate
- When generating a (pseudo)random value for the change in stock price each day, you
    may determine the level of decimal precision that you would like to use.
- Ensure that your prompts and output are crisp, professional, and well-formatted. For
    example, ensure that you have used spaces appropriately and checked your spelling.
- Adding comments in your code is encouraged. You may decide how best to comment
    your code. At minimum, please use a comment at the start of your code to describe its
    basic functionality.


