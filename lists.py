# Lists: ordered, mutable, allows duplicate elements
from operator import itemgetter
from re import M

# Makes printing list easier for me
def print_list():
    print(my_list)


#my_list = ['banana', 'cherry', 'apple']
my_list = [0] * 5
print_list()

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

