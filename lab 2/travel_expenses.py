# Ask the user for the number of times they rode the bus last month
rides = int(input('How many times did you ride the bus last month? '))
# Ask the user for the cost of one bus ride
fare = int(input('How much did one ride cost? '))
# Calculate the total cost of riding the bus last month. Multiply the two variables and store the result in a new variable.
total_cost = rides * fare
# Print the number of rides, the cost of one bus ride, and the total cost for the user. Convert numeric variables to strings.
print('Last month you rode the bus ' + str(rides) + ' times, and each ride cost, $' + str(fare) + ' your total ride cost this month was, $' + str(total_cost))