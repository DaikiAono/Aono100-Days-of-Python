from art import *
import random


# Computer_choice is a function that generates a random number
# within the range of the rps list to select a choice(rock, paper or 
# scissors)
def computer_choice(rps):
    comp_choice = random.randint(0, 2)
    print("Computer chose:")
    display_choice(comp_choice, rps) # This function is called
    # to display the results of computer choice.
    return comp_choice
    

# This function simply displays the ascii art of rock, paper or scissors
# It uses the choice select from user and computer and displays respectively.
def display_choice(choice, rps):   
    if choice == 0:
        print(rps[0])
    elif choice == 1:
        print(rps[1])
    elif choice == 2:
        print(rps[2])
    else:
        print("Invalid Choice")
        main()


# This is the game function that determines who wins, looses or ties.
def game(choice, comp_choice):
    # events of computer winning
    if choice == 0 and comp_choice == 1:
        print("Computer Wins")
    elif choice == 1 and comp_choice == 2:
        print("Computer Wins")
    elif choice == 2 and comp_choice == 0:
        print("Computer Wins")


    # events of player winning
    if choice == 0 and comp_choice == 2:
        print("You Win")
    elif choice == 1 and comp_choice == 0:
        print("You win")
    elif choice == 2 and comp_choice == 1:
        print("You win")


    # events of a tie
    elif choice == comp_choice:
        print("It's a tie!\nPlay again")
        main()


# The main function that calls unto the other functions and
# prompts the user to make a choice.
def main():
    rps = [rock, paper, scissors]

    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2" \
    " for Scissors.\n"))
    print("Your choice:")
    display_choice(choice, rps)

    
    comp_choice = computer_choice(rps)
    game(choice, comp_choice)


main()


