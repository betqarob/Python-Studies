# There are three different types of built-in data types that is used to store collections of data

# List and Tuples are allowed to containe duplicates! 
# Lists and Sets are mutable, meaning the internal state can be changed

'''List'''
list = [1, 3, 3, 7]
print(list[1])

'''Tuple'''
# Tuple is immutable, meaning that you cannot change its internal state
tuple = (1, 3, 3, 7)
print(tuple[3])

# this works in both list and tuples but not Sets/Dictionaries
tns_tuple = ('N', 'e', 'w', 'S', 't', 'a', 'c', 'k', 'R', 'o', 'k', 's')
print(tns_tuple[0])

#Tricky part of tuples
n_tuple = ("kubernetes", "cloud native", [8, 6, 7, 5, 3, 0, 9])

#lets say that I want to print out the letter 'e' from "kubernetes".. I'd have to reference the tuple and the index
print(n_tuple[0][3]) #referenes the first tuple and then the index of that tuple!

# We can access a range of the elements using slicing!
print(tns_tuple[0:3]) # returns N, e W
print(tns_tuple[3:8]) # would return the last remaining elements in the tuple


'''Set'''
# unable to contain duplicates (so the other 3 in the set will be ignored)
# this can't be changed via indexing or slicing
# doing set[1] will give a TypeError: 'set' objkect is not subsriptable
set = {1, 3, 3, 7}
print(set)


'''Now that there is a small understanding of what all three of them does.. 
Lets talk about when to use a List or a Tuple!'''

# A list should be used when you need to mutate your collection
# such as removing or adding new items to your collections

# A tuple should be used when you don't want your data to be changed.
# Are faster tan lists and should be used when we are defining constant set of values.

# Set uses Has Table as an its underlying data structure, so its really quick in locationg if an element exists within it.
# Set/Dictionary is used only if you don't need to store duplicates.



'''Concatentation and Repetition with tuples'''
print (('t', 'h','e') + ('S','h','i','b', 'a') + ('b', 'a', 'r', 'k', 's')) # the + operator is used in concatenation

print(("Shiba",) * 3) # the * operator is used in order to create repetitions

# since there is duplicates in the tuple, you can actually count the amount of dups there is!
print(tns_tuple.count('k')) # this returns 2
