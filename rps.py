import string
import random

print("Winning Rules for the game as follows: \n"
+ "Rock vs paper -> paper wins \n" + "Rock vs Scissor -> Rock wins \n" + "paper vs Scissor -> scissor wins")

while True:
    print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")

    choice = input("User turn: ")

    
    if choice == 'R':
        choice_name = 'Rock'
    elif choice == 'P':
        choice_name = 'paper'
    elif choice == 'S':
        choice_name = 'scissor'
    else:
        choice = input('Enter valid input: ')


    print('user choice is: ' + choice_name)
    print('\n Now its computer turn.......')


    comp_choice = random.choice('RPS')


    if comp_choice == 'R':
        comp_choice_name = 'Rock'
    elif comp_choice == 'P':
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    
    print('Computer choice is: ' + comp_choice_name)
    print(choice_name + ' V/s ' + comp_choice_name)

    
    if((choice == 'R' and comp_choice =='P') or (choice =='P' and comp_choice =='R')):
        print('paper wins => ', end='')
        result = 'paper'
    elif((choice == 'R' and comp_choice =='S') or (choice =='S' and comp_choice =='R')):
        print('Rock wins =>', end='')
        result = 'Rock'
    elif((choice == 'P' and comp_choice =='S') or (choice =='S' and comp_choice =='P')):
        print('scissor wins =>', end='')
        result = 'scissor'
    else:
        print('No Winner ', end='')


    if result == choice_name :
        if result != comp_choice_name:
            print(' <== User wins ==>')
    elif result == comp_choice_name:
        if result != choice_name:
            print(' <== Computer wins ==>')
    print('\nDo you want to play again? (Y/N)')
    ans = input()

    if ans == 'n' or ans == 'N':
        break
    elif ans == 'y' or ans == 'Y':
        continue
    else:
        break

print('\n Thanks for playing')