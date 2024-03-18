cents = int(input('How many cents do you have?: '))  # asks how many cents you have and stores as an int
if cents == 100:
    print('you have exactly one dollar.')
elif cents <= 100:  # elif statements are if the previous conditions are not met try this
    print('You have less than one dollar.')
elif cents >= 100:
    print('You have, ' + str(cents // 100) + ' dollars, and ' +  str(cents % 100) + ' cents')
# in the line above, its str, then the input value integer divided by a whole dollar, str
# then the remainder is expressed by using the % operator
