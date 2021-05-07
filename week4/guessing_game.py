import random

random_numnber = int(random.randint(1, 9))

print('############################################################')
print('                   Number Guessing Game                     ')
print('############################################################')

player_name = input('Enter your name: ')

print('Hi, {}.'.format(player_name))

player_input = input('Hit any key to begin. To quit any time, type "exit" ')

while player_input.lower() != 'exit':
    try:
        player_input = input('Pick a number between 1 and 9: ')

        if int(player_input) < 1 or int(player_input) > 9:
            raise ValueError('Please enter a number between 1 and 9 only ... ')

        if player_input.lower() == 'exit':
            break

        if int(player_input) == random_numnber:
            print('You guessed it!')

            random_numnber = int(random.randint(1, 9))

            print('Let''s play again ... ')

            continue

        elif int(player_input) > random_numnber:
            print('Guess lower .. ')

        elif int(player_input) < random_numnber:
            print('Guess higher .. ')

    except ValueError as err:
        if player_input.lower() == 'exit':
            print("Thank you for playing. Good bye!")
            break

        print('Invalid entry ... ')
else:
    print("Thank you for playing. Good bye!")