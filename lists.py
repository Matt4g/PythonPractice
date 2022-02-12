# Lists: ordered, mutable, allows duplicate elements
from operator import itemgetter
from re import M

# Makes printing list easier for me
def print_list():
    print(my_list)

#region Original main List I used
#my_list = ['banana', 'cherry', 'apple']
#print_list()

# Can have int, bool, string, and multiple of same type in a list
#my_list2 = [5, True, "apple", "apple"]
#print(my_list2)
 
 # Print a specific item from the list
# #item = my_list[0]
#print(item)

# Will print every item in the list individually
#for i in my_list:
 #   print(i)
 
 #region Will tell you if there is a specific item in the list
 # 
#if  'banana' in my_list:
 #    print('yes')
#else:
 #   print('no')

#if  'lemon' in my_list:
 #    print('yes')
#else:
 #   print('no')
#endregion
 
 # Tells you length of list
#print(len(my_list))

#region Adding Items
# Inserts item at the end of a list
#my_list.append('lemon')
#print_list()

# Insert item at specific spot in list
#my_list.insert(1, 'blueberry')
#print_list()
#endregion

#region Removing items
# Returns and removes last item in list
#tem = my_list.pop()
#print(item)
#print_list()

# Removes specific item from a list
#item =  my_list.remove("cherry")
#print_list()

#Removes everything from a list
#my_list.clear()
#print_list()
#endregion

# Reverses the list
#my_list.reverse()
#print_list()

#Sorts items in acsending order
#my_list_num = [4, 3, 1, -1, -5, 10]
#my_list_num.sort()
#
#new_list = sorted(my_list_num)
#print(my_list_num)
#print(new_list)
#endregion

#region 2nd main List used
# Can have 1 item and multiply to make 5 of that same item
#my_list = [0] * 5
#print_list()

#my_list2 = [1, 2, 3, 4, 5]
#
## Adds lists together
#new_list = my_list + my_list2
#print(new_list)
#endregion

#region 3rd main List used
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print_list()

#region Grab different parts of the list

## Grab between chosen starting position and ending position
#a  = my_list[1:5]

##Grab from start of list to chosen ending position 
#a  = my_list[:5]

##Grab from chosen starting position to the very end
#a  = my_list[1:]

## Can add a step to change how many of the values to print
#a  = my_list[::2]
###Can be negative to reverse the list
#a  = my_list[::-1]

#print(a)
#endregion

#endregion