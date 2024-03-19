for attempt in range(1, 4):
    attempt = input('What is the state capital of Wisconsin? ')  # it's madison
    remaining_attempts = 2
    if attempt != 'madison':
        remaining_attempts = remaining_attempts - 1
    elif attempt.upper() == 'MADISON':
        remaining_attempts = remaining_attempts - 1
        print(f'Correct, you got it with {remaining_attempts} guesses left')
        break
else:
    print('You ran out of attempts, the answer is Madison')

