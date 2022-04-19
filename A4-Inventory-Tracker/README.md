# MIS 315 ASSIGNMENT 4 :

# INVENTORY TRACKER

Completed November 2nd, 2020 (11/2/2020)

Your assignment is to create a Python program that assists a warehouse in tracking its
inventory. Your program should maintain up-to-date records on inventory data and allow the
user to both load new inventory data and analyze existing inventory data. The program should
ask the user if they would like to perform any additional analyses and allow the user to perform
an unlimited number of analyses.

Each CSV file that your program will analyze should follow the same basic format as the
following (this CSV file is posted alongside the assignment as **new_inventory1.csv** ). The CSV
files provided alongside this assignment are intended as _examples_ ; your program should be
able to handle any CSV files of this format. Each CSV file should consist of five columns. The first
column contains the inventory item’s ID; the second column contains the inventory item’s
name; the third item contains the inventory item’s quantity; the fourth column contains the
inventory item’s price; and the fifth column contains the inventory item’s shelf space (square
feet)).

```
341351 KwikTek Basic Keyboards 200 19.99 4.
856735 KwikTek Pro Keyboards 150 59.99 4.
137967 KwikTek Mice 40 1 9. 99 2.
402962 KwikTek USB Cables 500 4 .99 1.
```
Your program should have two distinct modes:

- Import: your program should ask the user for a CSV file to import. Data from the
    imported file should be added to the end of **inventory_records.csv**. If
    **inventory_records.csv** does not exist, then your program should create it. When adding
    this new data, check that inventory item’s ID does not already appear in
    **inventory_records.csv** (that is, a duplicate item). If the item is a duplicate, print out a
    message stating that the ID was already recorded, and do not add the item an additional
    time. After adding the new data, print out how many new items were successfully
    loaded, not counting duplicates.
- Statistics: your program should report how many distinct types of inventory are stored
    in **inventory_records.csv** (that is, the number of rows) and the total shelf space of the
    items in inventory. The warehouse does not worry much about pricing; they leave that
    to sales.


If the user requests an analysis other than import or statistics, then alert the user that the
requested analysis is not supported and ask them to try again.

Some considerations as you write your program:

- When your program asks the user for a CSV file to analyze, consider the possibility that
    the user asks for the analysis of a CSV file that does not exist or otherwise cannot be
    loaded successfully. Ensure that your program can handle this case and prints out an
    appropriate message indicating to the user that the file could not be found.
- You may assume that the CSV files that the program will read will be well-formatted.
    They will always contain the same five columns in the same order as above. Moreover,
    the quantity, price, and shelf space will always be well-formatted positive numbers. The
    quantity will always be a whole number.
- Write your code such that the entirety of your program is case insensitive (for example,
    the program would behave equivalently if the user enters “yes”, “Yes”, or “YES” or if
    they enter “import” or “IMPORT”).
- Ensure that your prompts and output are crisp, professional, and well-formatted. For
    example, ensure that you have used spaces appropriately and checked your spelling.
- Adding comments in your code is encouraged. You may decide how best to comment
    your code. At minimum, please use a comment at the start of your code to describe its
    basic functionality. If your code makes use of functions, then ensure that those
    functions contain appropriate docstrings.


Please use the following as a template for the tool’s expected functionality. Two CSV files
referenced below, **new_inventory 1 .csv** and **new_inventory 2 .csv** , are posted online alongside
this assignment. However, **new_inventory 3 .csv** does not exist and is an example of a bad
request that a user may make when using the program: