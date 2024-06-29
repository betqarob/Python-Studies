# Just a python file to understand variables (simple stuff). As mention this is used as a refresher
''' Do note: The way that variables work in python is different in other coding
languages! For example, in Java, I'd have to decleare a variable as a String, Int,
bool, long, etc.. With Python, whatever data I add into the variable, it will automatically
store as said variable type.'''

# boolean variable type
test1 = True

if (test1 != True):
    print("This variable is false!")
else:
    print ("This variable is true!")

# int variable type
number = 20

print (number + 30) # should print out the sumation of the expression inside

# string variable type

sentence = "This is a string variable! This can be used to store string variables!"

print (sentence) 

''' Additionally, these are helpful when recieving user-input! A user can input a value
and it can be storted as a String for the time being, and you'd have the ability to change the variable type as well!'''

testing = "8"


print (int(testing) + 436)

'''Example of User Input!'''

age = input("Enter your age: ")

# just to demonstrate the error we get
# print (age + 3) returns an error since age is considered a string!
# this can change by doing this (Type Conversions)

print("In 4 years you'll be:", int(age) + 4) 


# Simple if-else statements to get the jist of it using user-input
# This is also known as Explicit Conversion

'''Convert the user's weight between Kilograms (K) and Pounds (L)'''
weight = float(input ("Please enter your weight: "))
weight_unit = input("is your weight in Kilograms(K) or Pounds(L)? ")

#lets make sure that the weight unit that is being added 

if (weight_unit.upper() == 'K'): #Checks if the unit entered was a K
    converted = weight / 0.45 # conversion of kg to lbs
    print("Your weight in Lbs is:", converted)
elif (weight_unit.upper() == 'L'): # checks if the unity entered was an L
    converted = weight / 2.205 # conversion of lbs to kg
    print("Your weight in kg is:", converted)
else:
    print("Please enter a valid weight unit!") #if the program is unable to find either letter, print this out.