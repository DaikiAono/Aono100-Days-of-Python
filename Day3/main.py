from art import logo

def game():
    print(logo)
    print("Welcome to Treasure Island.\nYour mission is to find the treasure.")



    choice_1 = input("You're at a cross road. Where do you want to go?\n Type 'left'\
    or 'right'\n").lower()


    if choice_1 == "right":
        print("You got eaten by hyenas. You loose!")


    elif choice_1 == "left":
        choice_2 = input("You've come to a lake. There is an island in the middle of" \
        " the lake\n Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()


        if choice_2 == 'swim':
            print("You get eaten by alligators. You loose!")


        elif choice_2 == 'wait':
            choice_3 = input("You arrive at the island unharmed. There is a house" \
            " with 3 doors. One red, one yellow and one blue. Which color do you" \
            " choose?\n").lower()


            if choice_3 == 'red':
                print("You walk into a room with scorpions and stung to death. " \
                "You Loose!")
            elif choice_3 == 'yellow':
                print("You walk into a room that's pitch black and fall into lava." \
                "You Loose!")
            elif choice_3 == 'blue':
                print("You walk into a room full of treasure. You win!")


game()