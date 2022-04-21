# MIS 515 ASSIGNMENT 10:

# COVID-TRACKER

Your assignment is to create a tool that allows the user to analyze live state-level data on the
coronavirus (COVID-19) pandemic. Your program should ask the user which location (state)
they would like to search and which statistic they would like to search. Optionally, the user
should be able to enter a start date and/or end date for their search. Your program should print a
table of the results of the user’s search and show an accompanying bar graph. Your program
should allow the user to perform an unlimited number of analyses.

The COVID Tracking Project maintains live and historical records on the coronavirus (COVID-
19) pandemic in the United States, accessible at
https://covidtracking.com/api/v1/states/daily.json. The data is formatted as a JSON array and is
similar to the datasets you have worked with on your past few assignments. An example of the
formatting is below:
```
{"date":20200403,"state":"AK","positive":157,"death":3,"hospitalized":15,"totalTestResults":
16,"deathIncrease":0,"hospitalizedIncrease":6,"positiveIncrease":14,"totalTestResul
tsIncrease":994},

{"date":20200304,"state":"WI","positive":1,"totalTestResults":20,"deathIncrease":null,"hospitali
zedIncrease":null,"pos itiveIncrease":null,"totalTestResultsIncrease":null}
```

Your tool should ask the user for the following:
- A location (state) to search. In the JSON data, states are abbreviated with capitalized two-
    letter acronyms. For example, “CA” refers to California.
- A statistic to search. The dataset contains several statistics in each record. For example,
    “positive” refers to the total number of confirmed positive cases; “death” refers to the
    number of deaths; “totalTestResults” refers to the total number of people tested; etc.
- A start date for the search. First, ask the user if they would like to include a start date.
    Then, if the user answers “yes”, then ask the user which start date they would like to use.
    Dates are stored in the JSON data under the “date” field as integers in YYYYMMDD
    format. For example, April 1, 2020 would be stored as 20200401. If the user does not
    want to use a start date, a possible approach is to use a start date of - 999999999.
- An end date for the search. First, ask the user if they would like to include an end date.
    Then, if the user answers “yes”, then ask the user which end date they would like to use.
    If the user does not want to use an end date, a possible approach is to use an end date of
    +999999999.

Please handle all user inputs case-insensitively. For example, a search for “positive” and a search
for “poSiTiVE" should yield the same result. An important consideration is that the JSON data
downloaded from the COVID Tracking Project uses some field names that are entirely
lowercased (e.g., “date”, “positive”) and some that include a mix of lowercase and uppercase
letters (e.g., “totalTestResults”, “positiveIncrease”). Assuming that the requests data from the
COVID Tracking Project API is stored in a variable called response, a simple solution is to use
response.text.lower() to convert all field names to lowercased versions.

Due to data availability, some fields in your dataset may be missing values (an example of this
appears above in the Wisconsin data for 03/04/2020). The json module will use a value of None
for these missing values. In these cases, please treat None as equivalent to 0.

Some considerations to note:

- Consider the possibility that the user requests a statistic that is not present in your dataset.
    In this case, print out an appropriate message stating that the statistic was not available
    and asking the user to try again.
- Consider the possibility that, when loading the dataset, some connection issue occurs
    (that is, a status code other than 200). Ensure that your code handles this case and
    provides the user with a helpful printout if it does occur.
- The examples on the following pages use rotated labels on the x-axis to improve the
    legibility of the bar graphs. To adjust this setting for the x-axis labels in matplotlib,
    plt.xticks(rotation = 90, ha = "right") was used. This is optional.
- Ensure that your prompts and output are crisp, professional, and well-formatted. For
    example, ensure that you have used spaces appropriately and checked your spelling.
    Ensure that graphs are appropriately titled and that axes are appropriately labeled.
- Adding comments in your code is encouraged. You may decide how best to comment
    your code. At minimum, please use a comment at the start of your code to describe its
    basic functionality