# MIS 315 ASSIGNMENT 2 :

# GRADEBOOK

Created September 29th, 2020 (9/29/2020)

Your assignment is to create a Python gradebook analyzer tool that will allow the user to
analyze students’ grades across multiple courses. The tool will first greet the user and explain
that it is a gradebook analyzer tool. It will then ask the user how many students are in the
course. For each student, the program will present the user with prompts to input each of the
student’s assignment scores, and then it will report that student’s average. After all grades are
entered, the tool will report the course average and the overall grade distribution in the course.
The tool will allow the user to run this analysis for as many courses as desired.

When the tool asks the user the initial question of how many students are in the course, you
may assume that the user will respond with an integer number (that is, no decimal students).
_[Optional/extra credit: ensure that the user indicates that there is at least one student in the
course; if not, continue prompting the user until they provide a value of at least one.]_

After determining the number of students in the course, prompt the user for each of that
student’s scores. Do not assume that each student has the same number of scores (for
example, some students may have submitted an assignment early); instead, allow the user to
enter as many scores as desired for each student. _[Optional/extra credit: the allowable score
range is 0 to 100. If the user enters a value outside this range, then show a short message
indicating that this score is invalid, and allow the user to continue entering new scores if
desired.]_ After the user indicates that they have entered all scores for a given student, show
that student’s course average. You may assume that each assignment is weighted equally when
calculating the average.

After all students’ scores have been entered, the tool should report the overall course average
(the average of students’ averages) and the course grade distribution. For the course grade
distribution, report the number of As, Bs, Cs, Ds, and Fs in the course. For the purposes of the
assignment, an average of 90+ is an A; an average of 80 – 89.9 is a B; an average of 70 – 79.9 is
a C; an average of 60 – 69.9 is a D; and an average below 60 is an F.

At the end of the program, prompt the user for whether they would like to analyze another
course. Allow the user to continue analyzing as many courses as desired.

Some considerations as you write your program:

- When your program asks the user for a response, consider the possibility that the user
    will respond in uppercase, lowercase, or mixed case letters (“YES”, “yes”, or “Yes”, for
    example). Ensure that your program can handle any of these possibilities appropriately.
- You may assume that the user indicates each numeric value with valid formatting.
- Ensure that your prompts and output are crisp, professional, and well-formatted. For
    example, ensure that you have used spaces appropriately and double-checked your
    spelling.
- Adding comments in your code is encouraged. You may decide how best to comment
    your code. At minimum, please use a comment at the start of your code to describe its
    basic functionality.