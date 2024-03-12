# Write a program that uses input to ask for your name. Save the name in a variable. If using tutors or ChatGPT, ask for hints, not a solution.
name = input('What is your name? ')
# Next, ask for the number of credits you are taking this semester. The number of credits is an integer number, so convert it to an int and save this number in a int variable.
current_credits = input(str('How many credits are you currently taking? '))
# Print a message with both variables. You will need to convert the number of credits to a string to print it.
print(name + ', is taking ' + current_credits + ' credits this semester.')
# For example, if your name was 'Sam' and you are taking 7 credits, your program will print 'Sam is taking 7 credits this semester'.
#
# If someone else runs your program, it should print a message for them. So if a user called 'Miriam' used your program, and was taking 12 credits, the program will print 'Miriam is taking 12 credits'.
#
# Test your program with different names and different number of credits.