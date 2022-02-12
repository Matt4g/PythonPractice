# Lists: ordered, mutable, allows duplicate elements
from operator import itemgetter

# Makes printing list easier for me
def print_list():
    print(my_list)


my_list = ['banana', 'cherry', 'apple']
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
