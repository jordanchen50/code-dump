##################################################
## Assignment 5: LOTTERY GAME INTERFACE
## Author: Jordan Chen
## Email: jordanchen50@gmail.com
## Class: MIS-315 Fall 2020
##################################################

import tkinter, tkinter.messagebox, tkinter.simpledialog, csv, random

lottery_list = []

def create():
    
    """This function will generate 1000 numbers for lottery pool"""
    
    #Generates the lottery pool numbers with random import
    with open("lottery.csv","w") as file:
        writer = csv.writer(file, lineterminator = "\n")
        for i in range(1,1001,1):
            lottery = random.randint(1,1000000)
            row = [lottery]
            writer.writerow(row)
            lottery_list.append(lottery)
    
    # Message box to show user a sucessful lotterypool was made
    tkinter.messagebox.showinfo("Success!", "Lottery Pool Created!")
    
def play():
    
    """This function allows user to input number and attempt to win lottery"""
    
    # User input through a dialogue box
    guess = tkinter.simpledialog.askinteger("Play", "Enter your number:", minvalue = 1, maxvalue = 1000000)
    
    try:
        with open("lottery_out.csv","r") as file:
            reader = csv.reader(file)
        
        # Checks user guess against lottery pool
        if guess in lottery_list:
            if guess % 7 == 0:
                tkinter.messagebox.showinfo("WOW!!!","Jackpot! You win $5,000!")
            else:
                tkinter.messagebox.showinfo("Congrats!","You win $100!")
        else:
            tkinter.messagebox.showinfo("Sorry...","You didn't win. Play again sometime soon.")
           
    # If user didn't create lottery.csv yet, this except will catch it and show a warning
    except:
        tkinter.messagebox.showwarning("Error!","Sorry, we couldn't open a valid lottery numbers file.")
       
# Starts tkinter box
root = tkinter.Tk()
root.title("Lottery")
root.configure(bg = "skyblue1")
root.geometry("400x100")

# Button for creating lottery pool
create_button = tkinter.Button(root, text = "Create Lotto Pool", command = create)
create_button.configure(bg = "thistle1")
create_button.pack()

# Button for allowing user to guess
play_button = tkinter.Button(root, text = "Play The Lottery", command = play)
play_button.configure(bg = "coral1")
play_button.pack()

# Executes the tkinter!
root.mainloop()