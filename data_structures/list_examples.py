# NOTE: To run parts of code, in VS Code, select lines you want to run and press shift+enter

###############
# LIST BASICS #
###############

# lists can have any element
my_list = [1, 2, 3, 4, 5]
my_list2 = ['a', 'b', 'c']
my_list3 = [1, 'a', "hello!"]
my_list4 = [] # empty list

# list basic methods
my_list.append(6) # add an element to list
print(my_list)
my_list.remove(2) # remove first matching element from list
print(my_list)

# accessing list
print(my_list[0]) # first element
print(my_list[2]) # third element
print(my_list[-1]) #last element
print(my_list[-2]) #2nd last element

# multi-dimensional lists
list_2d = [[1, 1], [1, 2],
           [2, 1], [2, 2]]
list_mix = [ 1, 2, [3, 4], [ 5, [6, 7]]]

################
# LIST METHODS #
################

my_list = [2, 3, 4, 5]

# insert elements at given index
my_list.insert(0, 1) # insert 1 at index 0
my_list.insert(0, 0)
print(my_list)

# pop elements from list
my_list.pop() # remove last element from list
print(my_list)
my_list.pop(2) # remove element at index 2
print(my_list)

# generate a range of numbers
my_list = range(5) 
print(list(my_list))
my_list = range(0,10,2)
print(list(my_list))

# length of list
print(len(my_list))

# count number of given element in list
print(my_list.count(4))

# sort given list
my_list = [6, 3, 1, 2, 5, 4]
sorted_list = sorted(my_list) # method that returns sorted list
print(my_list)  # sorted does not modify original list
print(sorted_list)

################
# LIST SLICING #
################
a = list(range(1,11))

#all give same output
print(a)
print(a[:])
print(a[:len(a)])
print(a[0:len(a)])

print(a[1:2]) #1 element
print(a[1:1]) #empty
print(a[1:3]) #2 elements

print(a[:-1]) #exclude last element
print(a[:-2]) #exclude last 2 elements

print(a[-1:]) #last element
print(a[-2:]) #last 2 elements

print(list(a[-3:] + a[:-3])) #rotate list by 3 elements forward
print(list(a[3:] + a[:3])) #rotate list by 3 elements backward

######################
# LIST COMPREHENSION #
######################
# SYNTAX: new_list = [<expression> for <element> in <collection>]
numbers = [2, -1, 79, 33, -45]
print(numbers)
no_if   = [num * 2 for num in numbers]
print(no_if)
if_only = [num * 2 for num in numbers if num < 0]
print(if_only)
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]
print(if_else)
