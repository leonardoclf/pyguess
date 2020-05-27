import random

welcome = """
        Welcome to Guess Game

    press 1 - to start game 
    press 2 - to quit     
"""


def game():

    #Random words from txt
    f = open("words_alpha.txt")
    words = f.readlines()
    secret_word = random.choice(words)


    lista_word = list(secret_word)
    lista_wordB = list(secret_word)
    player_health = 10
    for n in range(len(secret_word)):
        lista_wordB[n] = "_"
    

    while True:
        print("\n" + "|".join(lista_wordB))
        guess = input(f"\nYou have {player_health} try: ")
        if guess in lista_word:
            for n in range(len(secret_word)):
                if secret_word[n] == guess:
                    lista_wordB[n] = guess         
        else:
            player_health -= 1 
            print(f"\nWrong! No {guess}.")
        if player_health < 1:
            print(f"\nYou fail! The word was: {secret_word}")
            print("\nGame Over")
            break
        elif lista_word == lista_wordB:
            print(f"\nYou guessed right: {secret_word}")
            print("\nYou won!")
            break
        


#GAME INIT
print(welcome)
choice = input("\n... ")

if choice == "2":
    exit()
elif choice == "1":
    game()
