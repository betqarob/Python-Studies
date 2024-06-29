# using this to randomly generate a list of words using PyEnchant
import enchant

wordList = enchant.Dict("en_US") # this just make sure that dictionary is set to English

baseList = open("dict-en.txt", "r")
lines = baseList.readlines()
baseList.close()

newWordList = open("dict-en_NEW.txt", 'w') # creates a new text file to have words
for line in lines:
    word = line.strip("\n")

    if wordList.check(word) == True:
        print(line + ' is valid. ')
        newWordList.write(line)
    else:
        print(line + ' is invalid')

newWordList.close()

# this was used using @Remfy's code on StackOverFLow (made it easier to generate a list of words)