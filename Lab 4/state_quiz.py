answer = input('What is the state capital of Wisconsin? ')  # it's madison

while answer.upper() != 'MADISON':  # converts input to uppercase then checks against the uppercase MADISON
    print('Sorry that was not correct, please try again.')
    answer = input('What is the state capital of Wisconsin? ')
    if answer.upper() == 'MADISON':
        answer.upper() == True
print('Correct!')

# clean up code as well as comment, don't forget to do quiz v2
