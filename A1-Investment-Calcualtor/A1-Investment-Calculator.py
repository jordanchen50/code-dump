##################################################
## Assignment 1: INVESTMENT CALCULATOR
## Author: Jordan Chen
## Email: jordanchen50@gmail.com
## Class: MIS-315 Fall 2020
##################################################

# Financial calculator for savings, CD, Mutual Funds, and Bonds calcualtions

print("Hello, welcome to the investment calculator! /n")

investment = input("Which type of investment would you like to make? (savings/CD/mutual funds/bonds) ")
amount = float(input("How much money would you like to invest? "))

# Calculate three years of savings at .6% compounded interset per year
if investment == "savings":
    savings_year1 = amount + (amount * .006)
    print("After 1 year:",savings_year1)
    savings_year2 = savings_year1 + (savings_year1 * .006)
    print("After 2 years:",savings_year2)
    savings_year3 = round(savings_year2 + (savings_year2 * .006),3)
    print("After 3 years:",savings_year3)
    
# Calculate Certificate of Deposit (CD)
elif investment == "CD":
    if amount >= 2500:
        cd_year1 = amount + (amount * .025)
        print("After 1 year:", cd_year1)
        
        #Round to 3 decimals so user can know percise cent amount, rounding to 2 decimals (normal cent format) can overshoot/undershoot true amount
        cd_year2 = round(cd_year1 + (cd_year1 * .025),3)
        print("After 2 years:", cd_year2)
        cd_year3 = round(cd_year2 + (cd_year2 * .025),3)
        print("After 3 years:", cd_year3)
        cd_year4 = round(cd_year3 + (cd_year3 * .025),3)
        print("After 4 years:", cd_year4)
    
    #Finds 1% interest for next 3 years for amounts less than $2500
    else:
        cd_year1 = round(amount + (amount * .01),3)
        print("After 1 year:", cd_year1)
        cd_year2 = round(cd_year1 + (cd_year1 * .01),3)
        print("After 2 years:", cd_year2)
        cd_year3 = round(cd_year2 + (cd_year2 * .01),3)
        print("After 3 years:", cd_year3)
        
# Calculate best case and worst case scenario mutual funds
elif investment == "mutual funds":
    print("Best Case Scenario:")
    mf_year1 = amount + (amount * .05)
    print("After 1 year:", mf_year1)
    mf_year2 = mf_year1 + (mf_year1 * .05)
    print("After 2 years:", mf_year2)
    mf_year3 = mf_year2 + (mf_year2 * .05)
    print("After 3 years:", mf_year3)

    print(" ------------------ ")
    
    print("Worst Case Scenario:")
    mf_year1 = amount - (amount * .01)
    print("After 1 year:", mf_year1)
    mf_year2 = mf_year1 - (mf_year1 * .01)
    print("After 2 years:", mf_year2)
    mf_year3 = mf_year2 - (mf_year2 * .01)
    print("After 3 years:", mf_year3)

# Calculate mutual bonds
elif investment == "bonds":
    if amount >= 5000:
        b_year1 = amount + (amount * .02)
        print("After 1 year:", b_year1)
        b_year2 = b_year1 + (b_year1 * .02)
        print("After 2 years:", b_year2)
        b_year3 = b_year2 + (b_year2 * .02)
        print("After 3 years:", b_year3)
    else:
        print("Sorry, the investmnet is not allowed because it is too small.")
        
# Catch any unexpected inputs for the financial calculator 
else:
    print("Sorry, this investment calcualtor does not support " + investment + ". Please try again and use savings, CD, mutual funds, or bonds.")

