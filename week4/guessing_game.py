import random

def show_score():
    print('###########################################')

    if len(attempts_list) > 0:
        if(min(attempts_list) > 1):
            print("     Your best score was {} attempts.".format(min(attempts_list)) + '\n')
        else:
            print('     Your best score was 1 attempt!\n')

    print("     Thank you for playing. Good bye!")
    print('###########################################')

def show_attempts(val):
    if(int(val) > 1):
        print('It took you {} attempts.'.format(val) + '\n')
    else:
        print('You did it in 1 attempt!\n')

attempts_list = []
num_range = 9
random_numnber = int(random.randint(1, int(num_range)))
attempts = 0
game_started = False

print('\n\n')
print('###########################################')
print('********** Number Guessing Game ***********')
print('###########################################')

player_name = input('\nEnter your name: ')

print('Hi, {}.'.format(player_name) +'\n')

player_input = input('Press Enter to begin. To quit any time, type "exit" ')

while player_input.lower() != 'exit':
    try:
        if(not game_started):
            player_input = input('\nEnter a number between 1 and ' + str(num_range) + ': ')

            game_started = True

        if int(player_input) < 1 or int(player_input) > int(num_range):
            print('That number is out of the range.')

            player_input = input('\nPlease enter a number between 1 and ' + str(num_range) + ': ')

            continue

        if player_input.lower() == 'exit':
            break

        if int(player_input) == random_numnber:
            print('You guessed it!')

            attempts += 1
            attempts_list.append(attempts)
            show_attempts(attempts)
            random_numnber = int(random.randint(1, int(num_range)))
            attempts = 0
            game_started = False

            print('Let''s play again ... \n')

            continue

        elif int(player_input) > random_numnber:
            player_input = input('Guess lower .. ')

            attempts += 1

        elif int(player_input) < random_numnber:
            player_input = input('Guess higher .. ')

            attempts += 1

    except ValueError as err:
        if player_input.lower() == 'exit':
            show_score()
            break

        print('Invalid entry! ')

        player_input = input('\nEnter a number between 1 and ' + str(num_range) + ': ')
else:
    show_score()