# Python uses pass-by-object-reference for parameter passing.
# When you pass an object to a function, the function receives a reference to the same object, not a copy

def modify_list(lst):
    lst.append(4) #modify the original list

my_list = [1, 2, 3]
print(my_list)
modify_list(my_list)
print(my_list)