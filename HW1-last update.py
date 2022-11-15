# Ali-Bagherzadeh HW2-MEM680
# at first give the user-name of game
print('Welcome to Rocks, Paper, Scissors Game!!')
# to allow the user to select the number of games that defines a win, we need this input:

while True:
    try:
        n = int(input('please let me know how many rounds of game you want to play by typing a number: '))
    except ValueError:
        print("Please enter a valid integer!")
        continue
    if n == int():
        print('thank you')
    break


b = 1         # to use in while
u = 0         # to use for counting user wins
c = 0         # to use for counting computer wins
import random
while b <= n:
            # getting input of user and exit command
    i = input("Enter letter of your choice (r for rock, p for paper, s for scissors) or exit: ")

            # to avoid mistakes in typing names input is just the first letter, but I need the full name to print the user choice.
    if i == 'r':
       user_choice = 'rock'
    elif i == 'p':
       user_choice = 'paper'
    elif i == 's':
       user_choice = 'scissors'
          # if the user wants to exit the game and type exit!
    elif i == 'exit':
        break
    else:                            # error handling if an input is not a valid choice
        user_choice = 'is not valid!'
        print('**input is not correct! please just use one of lowercase letters: "r", "p", "s" or exit')
        b = b-1                        # to not counting this as a game round!

          # computer choose randomly
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

          # game structure
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
            u = u+1                                          # counting user wins
        else:
            print("Paper covers rock! You lose.")
            c = c+1                                          # counting computer wins
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
            u = u+1
        else:
            print("Scissors cuts paper! You lose.")
            c = c+1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
            u = u+1
        else:
            print("Rock smashes scissors! You lose.")
            c = c+1

    b = b+1                                                  # to exit of while when user played n times!
if u > c:                                                    # Tells the player who won the overall game
    print(' => you won overall!')
elif u == c:
    print(' => the game was win/win!')
else:
    print(' => you lose overall!')
print('********* Thank you! Game is Over *********')