#Hangman games
import random

list_of_words = ["butt", "booty", "ass", "pawg"] 

def hangman(word):
    wrong = 0 #Checks for how many wrong answers the player has had.
    stages = ["",#The drawing of the Hanged man, stored in a list, to be joined later.
             "__________      ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word) #Creates a list out of the input by the game master.
    board = ["_"] * len(word)#First board of blank spaces.
    win = False; #Self explained
    print("Welcome to Hangman") #Runs only once.

#Loop breaks when to many tries has been made or when all letters have been guessed.
    while wrong < len(stages) - 1: #If we still haven't build the entire hangedman.
        print("\n")#Creating some space.
        msg = "Guess a letter" #Message in a variable, instead of directly because it keeps repeating.
        char = input(msg) #Takes a single letter from player
        if char in rletters: #If user inputs is on list...
            cindex = rletters.index(char) #Find index of were the character should go.
            board[cindex] = char #Change the displayed underscore with the char guessed by player.
            rletters[cindex] = '$' #Puts a money sign so that repeated letters can be guessed.
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True;
            break

#Outside the loop.
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))


rand_word = list_of_words[random.randint(0, len(list_of_words)-1)]
hangman(rand_word)
