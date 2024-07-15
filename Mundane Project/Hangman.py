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
            cWord = chosen_word()
            #start the game
            startGame(cWord)
        
def startGame(word):
    # variables that will be updateed as the game continues
    len_of_word = len(word)
    letters_guessed = []
    attempts_wrong = 0
    guess_index = 0
    current_guesses = 0
    
    for l in word:
        print(f"_", end=" ")
    print(word)
    #starts the game
    while (attempts_wrong != 7 and current_guesses != len_of_word):
        print(f"\nCurrent letters you've guessed: \n{letters_guessed}")
        
        guess = input("Enter the letter you want to guess: ")

        # makes sure the length of the guess is a single character. 
        if (len(guess) > 1):
            print("Please enter a single letter! Try again")
        else:
            # guesses incorrectly
            if (word[guess_index].lower() != guess):
                print("Incorrect! Try again!")
                attempts_wrong += 1 # will be incremented as a result of wrong guesses
                letters_guessed.append(guess)
                # print the board with the lines under
                print(create_board(attempts_wrong))
                current_guesses = printWord(letters_guessed, word)
            else:
                # guesses correctly
                print("Correct! \n")
                print(create_board(attempts_wrong))
                guess_index += 1 #will increase the index and allow to keep track of the current spot in the word we are in
                letters_guessed.append(guess) 
                current_guesses = printWord(letters_guessed, word)
        
        if (current_guesses == len_of_word):
            print(f"/n Gamve is over! You've completed the game with {7 - attempts_wrong} attempts left! Thank you for playing :D! ")
            break
        
        if(attempts_wrong == 7):
            print("Game over! You've used all your attempts. Thank you for playing!")

            


    
            
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
    |     /|"\"
    |
    |
    |
    =========
    """,
    """
    --------
    |      |
    |      o
    |     /|"\"
    |      |
    |
    |
    =========
    """,
    """
    --------
    |      |
    |      o
    |     /|"\"
    |      |
    |     /
    |
    =========
    """,
    """
    --------
    |      |
    |      o
    |     /|"\"
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

def printWord(guesses_list, word):
    # printing the word with dashes in them as well as the board
    count = 0
    letters_right = 0
    for c in word:
        if c.lower() in guesses_list:
            print(word[count], end=" ")
            letters_right += 1
        else:
            print("_", end=" ")
        count += 1
    return letters_right

    
def search_letter(letter, list):
    for l in list:
        if (l == letter):
            return 
# this line of code just starts the program.
if __name__ == "__main__":
    main()