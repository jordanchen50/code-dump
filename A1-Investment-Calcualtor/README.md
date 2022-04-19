# MIS 315 ASSIGNMENT 1:
# INVESTMENT CALCULATOR

Created September 13th, 2020 (9/13/2020)

Your assignment is to create a Python investment calculator tool that will allow the user to
project the multi-year returns for a range of investment strategies. The tool will first greet the
user and explain that it is an investment calculator tool. It will then ask the user for (1) a type of
investment to project and (2) how much money they would like to invest. Finally, the tool will
perform the calculations described below and output a multi-year projection.

Each investment strategy incorporates compound interest. For example, suppose that the user
wants to invest $100, and the interest rate is 5%. After a year, the user’s investment would be
worth $100 x 1.05 = $105. After another year, since the investment had already increased in
value to $105, the user’s investment would be worth $105 x 1.05 = $110.25. Optionally, the
calculation for the value of the investment after several years can be performed in one step:
initial investment x rateyears. For example, to calculate the value of the investment after two
years, $100 x 1.05^2 = $110.25.

The tool should support the following investment strategies:
1) **Savings**. The investment returns 0.6% per year for three years.
2) **CD**. For investments of at least $2,500, the investment returns 2.5% per year for four
years. For all other investments, the investment returns 1% per year for three years.
3) **Mutual funds**. The investment’s performance depends on the stock market; determine
both a best-case and worse-case scenario. In the best-case scenario, the investment
returns 5% per year for three years. In the worst-case scenario, the investment loses 1%
per year for three years.
4) **Bonds**. For investments of at least $5,000, the investment returns 2% per year for three
years. Investments under this amount do not qualify; if this occurs, output a message
stating that that the investment was not allowed because it was too small.

Some considerations as you write your program:

- You may assume that the user indicates each investment type using the appropriate
    capitalization. For example, if they are interested in analyzing mutual funds, you may
    assume that they enter “mutual funds” as opposed to “MUTUAL FUNDS”, “Mutual
    Funds”, etc.
- You may notice in the examples above or as you test your program that Python
    sometimes includes odd decimal places (for example, 1157.6250000000002 above).
    Python’s decimal computations include some minor imprecision, resulting in extra
    decimals. Optionally, this issue is fixable using the round() function. The round() function
    takes two values: the number to round, and the number of decimal places to include in
    the output. For example, round(1157.6250000000002, 3) will round to three decimal
    places, or 1157.625.
- You may assume that the user indicates the amount of the investment that they would
    as a well-formatted numeric value.
- It is possible that the user will ask for an investment type that you have not considered.
    For example, perhaps the user will ask to analyze money markets. Although you do not
    have the necessary investment details, please give the user an appropriate warning
    message and ask them to try again (for example, “Sorry, this investment calculator does
    not support money markets. Please try again using savings, CD, mutual funds, or
    bonds.”)


- Ensure that your prompts and output are crisp, professional, and well-formatted. For
    example, ensure that you have used spaces appropriately throughout your application.
- Adding comments in your code is encouraged. You may decide how best to comment
    your code. At minimum, please use a comment at the start of your code to describe its
    basic functionality.