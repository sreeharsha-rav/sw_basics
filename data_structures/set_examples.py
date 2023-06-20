##############
# SET BASICS #
##############

# initializing a set
my_set = {"basics", True, 21, 3.14, 'A'}    # set can have any data type, but no duplicates allowed
print(type(my_set))
print(my_set)   # set is unordered, observe the output
print(len(my_set))  # number of items in set

# accessing set
for item in my_set: # cannot access items through index/key, access only by looping through set
    print(item)

# adding items to set
my_set.add("hello") # adding single item
print(my_set)

my_set2 = {"hi", "welcome"}
my_set.update(my_set2)  # adding multiple items, can be a set
print(my_set)

my_set.update([2,3,4])  # can also be a list
print(my_set)

# removing items from set
my_set.remove('hi') # removes single item, however raises error if item does not exist
print(my_set)

my_set.discard(2)   # removes single item, but does not raise error if item does not exist
print(my_set)

random_item = my_set.pop()  # remove a random item from set
print(random_item)
print(my_set)

my_set.clear()  # empty the set
print(my_set)

del my_set2 # delete the set
try:
    print(my_set2)
except:
    print("DELETED SET: Set does not exist")