state = str(input('What state are you considering to run for?: '))
age = int(input('How old are you?: '))
if age >= 30:
    age_el = True  # if input matches conditions its set as true
else:
    age_el = False  # these else statements are set up for line 16 down to print the conditions of false
citizenship = int(input('How many years have you been a citizen for?: '))
if citizenship >= 9:
    citizenship_el = True
else:
    citizenship_el = False
current_state = str(input('Which state do you currently reside in?: '))
if state == current_state:
    state_el = True
else:
    state_el = False
if age_el and citizenship_el and state_el == True: # I also had a question about my error messages here.
    print('You are eligible!')
else:
    if not age_el:
        print('you are too young.')
    if not citizenship_el:
        print('You have not been a citizen long enough.')
    if not state_el:
        print("Your chosen state and state of residence don't match")
    print('You are not eligible.')  # if directed to the else this will print regardless of the lack of qualification
    # message
