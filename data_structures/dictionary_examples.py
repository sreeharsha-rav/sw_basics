#####################
# DICTIONARY BASICS #
#####################

# initialzing a dictionary
my_dict = {}
my_dict = {'name': 'Harsha', 'age': 25, 'AI': False}    # key-value can be of any data type, but keys are always unique
print(type(my_dict))
print(my_dict)

# accessing dictionary
print(my_dict.keys())   # print all keys in dictionary
print(my_dict.values()) # print all values in dictionary
print(my_dict.items())  # print list of key:value pairs

print(my_dict['name'])  # provide key to get associated value
print(my_dict.get('age'))   # get value for given key

# adding items in dictionary
my_dict['gender'] = 'male'
print(my_dict)

my_dict.update({'fav food': 'curry'})
print(my_dict)

# changing items in dictionary
my_dict['name'] = 'Adam'
print(my_dict)

my_dict.update({'fav food': 'pizza'})
print(my_dict)

# removing items from dictionary
my_dict.pop('age')  # remove given key and associated value
print(my_dict)

my_dict.popitem()   # remove last added item
print(my_dict)

my_dict.clear() # empty all items from dictionary
print(my_dict)

del my_dict # delete dictionary