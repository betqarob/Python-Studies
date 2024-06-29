# This file is used to relearn the basics of Python before moving forward
# towards learning frameworks and more advance topics of coding

# Used to make sure Python is installed and working properly
print("Hello World")

# Code blocks are denoted by line indentation (which is different from other coding languages)
if True:
    print("This is how line indentation works")
else:
    print("I tried lol")

#On top of that, I can also make multi-line statements using the character (\)

# I could also declare multiple variables at once as long as I use the character (,)
# to seperate data values 

price_1, price_2, price_3 = 2, 3, 4

sum = price_1 + \
    price_2 + \
    price_3 

print(sum)

# If I'm using chartacters like [], {}, (), the line continuation character is not needed

days = ['Monday', 'Tuesday', 'Wednesday', 
        'Thursday', 'Friday']

# Quotations are used for strings values... """can be used for long string input"""

paragraph = """I don't know what to type here but I'm going to type something that
is meaningful... I guess this is long enough right?"""

print(paragraph)


#I've already used comments all throughout this file....

'''
But I haven't used this yet so.. Yeah I can make a multiline comment :D
'''

# This is new to me but, you can create inputs that awaits for the user to take action
# raw_input("\n\nPress the enter key to exit.")

#I can make multiple statements in a single line! Ex:

import sys; x = 'foo'; sys.stdout.write(x + '\n') #could be helpful as long as neither statement starts a new code block

# Single code blocks withing a group of individual statements are known as *Suites*
# Compound or Complex statements, such as if, while, def, and class require a header and a suite!

# if expression, elif, and else are considered headers. Everything inside those blocks 
# are known as suites!
#  
'''if expression: 
    suite
elif expression :
    suite
else : 
    suite'''