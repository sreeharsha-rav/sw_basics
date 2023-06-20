################
# TUPLE BASICS #
################

# initializing tuple
my_tuple = ('Harsha', 21, 'student', 'ASU')
print(my_tuple)
print(type(my_tuple))   # get type of data structure
print(len(my_tuple))    # number of elements in my_tuple

# accessing tuple
print(my_tuple[0])  # similar to accessing lists
print(my_tuple[-1])
print(my_tuple[0:2])

# updating tuple
try:
    my_tuple[1] = 'Martin'  # update a value in tuple
    print(my_tuple)
except:
    print("UPDATING TUPLE: Cannot change values in my_tuple")

# unpacking a tuple
name, age, role, uni = my_tuple # order matters
print(name, age, role, uni)

# deleting tuple
del my_tuple    # delete tuple
try:
    print(my_tuple) # printing deleted tuple
except:
    print("DELETED TUPLE: my_tuple does not exist")

# 1 element tuple
my_tuple = (1,)
print(my_tuple)

# generating tuples from lists, list of tuples
names = ["Adam", "Bob", "Charles"]
ages = [20, 30, 40]

info = zip(names, ages)
print(info)                 # zip object
print(list(info))