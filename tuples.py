#imports a from lists.py to use as an example
import lists

# Tuple: ordered, immutable, allows duplicate elements
#myTuple = ('Max', 28, 'Boston')
# Doesnt have to have parenthesis 
myTuple = 'Max', '28', 'Boston'

#region Basics
# Shows how to change list into tuple
#myTuple = tuple([lists.a])

#item = myTuple[1]

#Tuples dont allow change so nothing will happen
#myTuple[0] = 'Tim'

#for i in myTuple:
    #print(i)
    
#if 'Max' in myTuple:
#    print("yes")
#else:
#    print("no")

#myTuple = 'a', 'p', 'p', 'l', 'e'

#print(len(myTuple))
#print(myTuple.count('p'))

#finds index of first instance of object
#print(myTuple.index('p'))

#Can convert Tuple to List and vice versa
#myList = list(myTuple)
#print(myList)
#myList.append('car')
#print(myList)
#myTuple = tuple(myList)

#Slicing behaves same as lists
#b = myTuple[0:2]
#print(b)
#endregion

#region More complicated
# Must match number of elements in tuple
#name, age, city = myTuple
#print(name)
#print(age)
#print(city)

#unpack tuple  between certain areas and turns into list
#testTuple = 0, 1, 2, 3, 4
#i1, *i2, i3 = testTuple
#print(i1)
#print(i3)
#print(i2) 

#Differences between lists and tuples
#Tuples can be optimized more by python
#import sys
#my_list = [0, 1, "hello", True]
#my_tuple = [0, 1, "hello", True]
#print(sys.getsizeof(my_list), "bytes")
#print(sys.getsizeof(my_tuple), "bytes")

#import timeit
#print(timeit.timeit(stmt = "[0, 1, 2, 3, 4, 5]", number=1000000))
#print(timeit.timeit(stmt = "(0, 1, 2, 3, 4, 5)", number=1000000))


#endregion

print(myTuple) 
#print(item)
