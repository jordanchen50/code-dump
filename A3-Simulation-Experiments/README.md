# MIS 315 ASSIGNMENT 3 :

# SIMULATION EXPERIMENTS

Created October 10th, 2020 (10/10/2020)

Your assignment is to create a Python program that simulates the weather. For the purposes of
this assignment, your program is meant to simulate whether there is sufficient rain to grow
crops. Each day, you may assume that the weather is one of the following states based on
random chance:

```
1) Heavy rain (5% chance) – rainfall of 3 inches.
2) Light rain (1 0 % chance) – rainfall of 1 inch.
3) No rain (8 5 % chance).
```
These chances can be simulated based on a (pseudo)random number. For example, suppose
that you were interested in simulating whether an archer’s arrow hits a target, and the archer is
generally successful in 80% of their tries. One way to simulate each try is to generate a random
number between 1 and 5. If the random number is between 1 and 4 (80% of the possibilities),
then we say the archer’s arrow hit the target; if the random number is 5 (20% of the
possibilities), then we say the archer’s arrow missed the target. The same idea can be applied
to simulating the different states of the weather.

Your program should continue simulating each day’s weather and print out the result for the
user to view until one or more of the following conditions are met. If one or more of these
conditions are met, then the simulation should stop:

```
1) Total cumulative rainfall since the beginning of the simulation is at least 8 inches. If this
occurs, then the soil is moist enough to begin planting crops.
2) 2 consecutive days of rain. If this occurs, then it must be the start of the rainy season,
and it is safe to begin planting crops.
3) 14 consecutive days of no rain. If this occurs, then it must be the start of a drought, and
we will need to think of planting crops elsewhere.
```
Once a simulation is complete, it should state which of the above conditions were met and
caused it to complete the simulation. The program should ask the user if they would like to run
the simulation again and allow the user to run the simulation an unlimited number of times.

Some considerations as you write your program:

- You do not need to write your own (pseudo)random number generator. Please feel free
    to import an appropriate module to handle generating (pseudo)random numbers. You
    do not need to set your own seed for the (pseudo)random number generator.
- It is possible for more than one of the stopping conditions above to be met in the same
    simulation. If this occurs, please print all stopping conditions that were met.
- When your program asks the user for a response, consider the possibility that the user
    will respond in uppercase, lowercase, or mixed case letters (“YES”, “yes”, or “Yes”, for
    example). Ensure that your program can handle any of these possibilities appropriately.
- Ensure that your prompts and output are crisp, professional, and well-formatted. For
    example, ensure that you have used spaces appropriately and checked your spelling.
- Adding comments in your code is encouraged. You may decide how best to comment
    your code. At minimum, please use a comment at the start of your code to describe its
    basic functionality. If your code makes use of functions, then ensure that those
    functions contain appropriate docstrings.