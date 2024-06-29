# This python file is to learn and understand Python Exceptions

'''There is two types of errors. Syntax Errors, which is an error that is caused by
a syntax mistake, and Exception Errors, which is a result of everything working as intented
and the result is an error!'''

# You can stop a program by raising an exception error! 

number = 10
if number >= 5:
    #raise Exception(f"The number should not exceed 5! ({number})")
    print(number)
# Everything worked as intended, and returned the error stating that number exceeded the limit!
# Also notice that the last line of code never executed. That is because the program stops at the exception part of the code


'''AssertionError'''
# This should only be used in order to debugg your program during development!
# AssertionError would make it so that your pogram runs as long as certain conditions are met.

tnumber = 1
assert(tnumber < 5), f'the number should not exceed 5. ({tnumber})'
print(tnumber)

# What will occur is that your assert will return as true, letting your program continue as intended!
# However, if the number was greater than 5, the program will raise an AssertionError!

assert(tnumber < 5), f'The number should not exceed 5. ({number})'
print(number)

# This should only be used when debugging! DO NOT use it to set constraits to your program.

'''Try and Except Coding'''
# The best way to set constraits to your program is using the Try statement!
# This would run your code and catch any exception that can occur, letting your program while ignoring exceptions
# This becomes useful when you want to catch these exception and log them into a file!

# Example:

# It doesn't matter what this function does, its only going to be used for the try-catch errors
def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux Systems.")
    print ("Doing Linux things.")

try:
    linux_interaction()
except:
    pass
# Everything passes but that is because pass allows the program to continue as normal
# even though linux_interaction() wasn't used since this isnt a linux operating system.

try:
    linux_interaction()
except:
    print("Linux function wasn't excuted")

# that can be changed however if we changeed pass to something else
# the output prints out the print statement we have inside the except

try:
    linux_interaction()
except RuntimeError as error:
    print(error)
    print("Linux function wasn't excuted")

# Note: if you have multiple lines of code inside a try statement and the program runs into an error
# the program will stop at were the error occurs and not execute the rest of the code.
