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

print(a[-1]) #last element
print(a[-2]) #2nd last element

print(a[:-1]) #exclude last element
print(a[:-2]) #exclude last 2 elements

print(a[-1:]) #last element
print(a[-2:]) #last 2 elements

print(list(a[-3:] + a[:-3])) #rotate list by 3 elements forward
print(list(a[3:] + a[:3])) #rotate list by 3 elements backward

#####################
# REMOVE DUPLICATES #
#####################

def remove_duplicates(dupe_list):
  new_list = []
  for i in range(len(dupe_list)):
    if not(dupe_list[i] in new_list):
      new_list.append(dupe_list[i])

  return new_list

print(remove_duplicates([1,1,1,2,3,5,5,6,7,7,7,7,7,7]))

###################
# MAX SUBLIST SUM #
###################
def maximum_sub_sum(my_list):
  max_sum = my_list[0]
  cms_sum = 0
  for i in range(len(my_list)):
    cms_sum += my_list[i]
    if cms_sum >= max_sum:
      max_sum = cms_sum
    elif cms_sum < 0:
      cms_sum = 0

  return max_sum

print(maximum_sub_sum([-1, -1, -2, -4, -5, -9, -12, -13]))
