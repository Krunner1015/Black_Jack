import p1_random as p1
rng = p1.P1Random()
# import the module (do this on the first line of code)
# create a P1Random variable

gameNum = 0 # number of games played / game # currently being played
playerHand = 0 # the hand of the player
my_number = int(rng.next_int(13) + 1) # A random number in range [1,13]
my_value = 0 # the dealers hand
player_wins = 0 # number of times the player won
dealer_wins = 0 # number of times the dealer won
ties = 0 # number of times the game ended in a tie

# identifies the name/value of your card
def card_value(my_number):
    if my_number == 1:
        print("Your card is a ACE!")
    elif my_number == 11:
        print("Your card is a JACK!")
    elif my_number == 12:
        print("Your card is a QUEEN!")
    elif my_number == 13:
        print("Your card is a KING!")
    else:
        print(f"Your card is a {my_number}!")

#displays the choice menu
def menu():
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")
    print("")

#Initiates the game
quit_game = False
while not quit_game:
    gameNum += 1
    print(f"START GAME #{gameNum}")
    print("")
    card_value(my_number)
    playerHand = playerHand + min(my_number,10)
    print(f"Your hand is: {playerHand}")
    print("")
    menu()
    playerChoice = int(input("Choose an option: "))

    #while loop to make the game end when the players hand is either greater than or equal to 21
    while playerHand < 21:
        #runs the procedure if the user selects option 1
        if playerChoice == 1:
            print("")
            my_number = int(rng.next_int(13) + 1)  # A random number in range [1,13]
            card_value(my_number)
            playerHand = playerHand + min(my_number,10)
            print(f"Your hand is: {playerHand}")
            print("")
            #checks if the players hand is equal to 21, displaying that the user won and starting the next game
            if playerHand == 21:
                print("BLACKJACK! You win!")
                player_wins += 1
                print("")
                my_number = int(rng.next_int(13) + 1)  # A random number in range [1,13]
                playerHand = 0
                gameNum += 1
                print("")
                print(f"START GAME #{gameNum}")
                print("")
                card_value(my_number)
                playerHand = playerHand + min(my_number,10)
                print(f"Your hand is: {playerHand}")
                print("")
                menu()
                playerChoice = int(input("Choose an option: "))
            #checks if the players hand is greater than 21, displaying that the player lost and starting the next game
            elif playerHand > 21:
                print("You exceeded 21! You lose")
                dealer_wins += 1
                print("")
                my_number = int(rng.next_int(13) + 1)  # A random number in range [1,13]
                playerHand = 0
                gameNum += 1
                print("")
                print(f"START GAME #{gameNum}")
                print("")
                card_value(my_number)
                playerHand = playerHand + min(my_number,10)
                print(f"Your hand is: {playerHand}")
                print("")
                menu()
                playerChoice = int(input("Choose an option: "))
            #otherwise continue the game as it was
            else:
                menu()
                playerChoice = int(input("Choose an option: "))

        #runs the procedure if the user selects option 2, with the dealer revealing its hand and checking who won the game, displaying accordingly, and starting the next game
        elif playerChoice == 2:
            my_value = rng.next_int(11) + 16  # A random number in range [16,26]
            print("")
            print(f"Dealer's hand: {my_value}")
            print(f"Your hand is: {playerHand}")
            print("")
            if my_value > 21:
                print("You win!")
                print("")
                player_wins += 1
                playerHand = 0
            elif my_value == playerHand:
                print("It's a tie! No one wins!")
                print("")
                ties += 1
                playerHand = 0
            else:
                print("Dealer wins!")
                print("")
                dealer_wins += 1
                playerHand = 0
            gameNum += 1
            print("")
            print("")
            print(f"START GAME #{gameNum}")
            print("")
            my_number = int(rng.next_int(13) + 1)  # A random number in range [1,13]
            card_value(my_number)
            playerHand = playerHand + min(my_number,10)
            print(f"Your hand is: {playerHand}")
            print("")
            menu()
            playerChoice = int(input("Choose an option: "))
        #runs the procedure if the user selects option 3, displaying the statistics of the game
        elif playerChoice == 3:
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {ties}")
            print(f"Total # of games played is: {gameNum - 1}")
            print(f"Percentage of Player wins: {(player_wins / (gameNum - 1)) * 100:.1f}%")
            print("")
            menu()
            playerChoice = int(input("Choose an option: "))
        #runs the procedure if the user selects option 4, quitting the game and the program
        elif playerChoice == 4:
            print("")
            quit()
        #displays an invalid message if the user tries to select an option that is not 1, 2, 3, or 4 and re-displaying the menu so the user can select a new option
        else:
            print("")
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
            print("")
            menu()
            playerChoice = int(input("Choose an option: "))