# MIS 315 ASSIGNMENT 5 :

# LOTTERY GAME INTERFACE

Completed November 14th, 2020 (11/14/2020)

Your assignment is to create a Python program that uses a graphical user interface (GUI) to
facilitate a small lottery. Your program should create a basic tkinter user interface. The user
interface should have a title of “Lottery” and a background color of “skyblue1”. Two buttons
should be displayed: first, a “Create lotto pool” button with a “thistle1” background color, and
second, a “Play the lottery” button with a “coral1” background color. (Note that the button
background colors may not display correctly on Macs). On a Windows 10 computer, 400x1 00
was found to be a good set of dimensions for the GUI, but you may experiment if those
dimensions do not work as well on your computer. In sum, the interface should reflect the
screenshot below. The screenshot below was created on a Windows 10 computer; the exact
appearance of your GUI may vary slightly depending on your computer.

When the user presses the “Create lotto pool” button, the program should create a CSV file
named **lottery.csv** (if this file already exists, then it should be completely overwritten). The
program should generate 1,000 rows of data, where each row is a single random number
ranging from 1 to 1,000,000. As an example, **lottery.csv** may look like the screenshot below
when opened in Microsoft Excel.

After **lottery.csv** is created, your program should show a popup indicating that the file was
written successfully as shown in the screenshot below.

When the user presses the “Play the lottery” button, they should be prompted for their lottery
number. There are two acceptable approaches to prompt the user for their lottery number. The
first approach (preferred) is to ask the user for their lottery number through a popup as follows
(note the additional import of tkinter.simpledialog):

The tkinter.simpledialog.askinteger() automatically converts the user’s
response to an int value stored in the guess variable. Moreover, if the user enters an invalid
value (a non-numeric value, a number less than 1, or a number greater than 1,000,000), they
are automatically shown another popup alerting them to the mistake and given the opportunity
to make a correction.

As an alternative, rather than tkinter.simpledialog.askinteger(), it would be
acceptable to prompt the user for their lottery number using input() instead and to handle
their responses through the shell. If you choose this option, please implement the same input
validation procedures (reprompt the user if they enter a non-numeric value, a number less than
1, or a number greater than 1,000,000).

Once the user’s number has been successfully entered, open **lottery.csv** and compare the
user’s number to the lottery numbers on file. If the user’s number is not on file, notify them
that they have lost through a popup.

If the user’s number is found in **lottery.csv** and is divisible by 7, then their number is lucky, and
they win the jackpot prize of $5,000. Alert the user through a popup.

Finally, if the user’s number is found in **lottery.csv** but is not divisible by 7, then they win a prize
of $100. Alert the user through a popup.

Some considerations as you write your program:

- You do not need to write your own (pseudo)random number generator. Please feel free
    to import an appropriate module to handle generating (pseudo)random numbers. You
    do not need to set your own seed for the (pseudo)random number generator.
- Consider the possibility that, when the user presses the “Play the lottery” button, the
    **lottery.csv** file does not exist (perhaps the user has not generated the lottery pool yet)
    or otherwise cannot be opened successfully. In this case, show an appropriate popup.
- Ensure that your prompts and output are crisp, professional, and well-formatted. For
    example, ensure that you have used spaces appropriately and checked your spelling.
- Adding comments in your code is encouraged. You may decide how best to comment
    your code. At minimum, please use a comment at the start of your code to describe its
    basic functionality. If your code makes use of functions, then ensure that those
    functions contain appropriate docstrings.


