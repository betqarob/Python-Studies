import random
import time

#main functions where everything will be handled
def main():
    print(f"Welcome to this little game of Hangman!\nTo keep it short and simple, Hangman is a game of attempting to guess the words with little attempts as possible!\nIf you use all your attempts (before the man is drawn), you lose! Word will randomly be chosen so do your best to guess!")
    queueGame = input("Do you want to play? (Y/N)").upper()

    #testing to make sure the queGame is working as intended
    # assert (queueGame == "Y"), f"Game ending... Thank you for your time ({queueGame})"
    match queueGame:
        case "N":
            print("Terminating file....")
            time.sleep(5)
            print("File terminated.")
        case "Y":
            startGame()
        
#function that will handle the game (should continue running until a false value is returned)
def startGame():
    while True:
        # randomly selects the word to start the game
        cWord = chosen_word()
        letters_guessed = [] # will keep track of the letters guessed
        attempts = 7 # amount of attempts given.

        # create a list that is filled with blanks to represent the letters needed to be guessed
        blanks = ["_"] * len(cWord)

        # wants to print the board and ask user for their input
        while (attempts != 0 and ("_" in blanks)):
            print(create_board(0), "\n", *blanks)
            #print(*blanks) # using * will print everything within an array
            break
        break
            
# project the board depending on the current attempts of the player
def create_board(attempt):
    board = (
        """
    --------
    |      |
    |
    |
    |
    |
    |
    =========
    """,
    """
    --------
    |      |
    |      o
    |
    |
    |
    |
    =========
    """,
    """
    --------
    |      |
    |      o
    |      |
    |
    |
    |
    =========
    """,
    """
    --------
    |      |
    |      o
    |     /|
    |
    |
    |
    =========
    """,
    """
    --------
    |      |
    |      o
    |     /|\
    |
    |
    |
    =========
    """,
    """
    --------
    |      |
    |      o
    |     /|\
    |      |
    |
    |
    =========
    """,
    """
    --------
    |      |
    |      o
    |     /|\
    |      |
    |     /
    |
    =========
    """,
    """
    --------
    |      |
    |      o
    |     /|\
    |      |
    |     / \
    |
    =========
    """
    )

    return board[attempt]

def chosen_word():
    # randomly chosing a word at random from a given list
    word_list = ["Judas", "Physics", "Biology", "Million", "Navigating", "Mundane",
                 "Awesome", "Batman", "Liberty", "Overcompensate", "Fiend", "Chaos", "Fantasy",
                 "Resolve", "Kingdom", "Malevolent", "Transfiguration", "Divergent", "Fluctuations", "Glamour"]
    
    word = random.choice(word_list)
    
    return word


# this line of code just starts the program.
if __name__ == "__main__":
    main()