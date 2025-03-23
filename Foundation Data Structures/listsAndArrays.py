# Some of the most commonly way to aggregate data in a Python program 
# is to use a Python list. A python list is an object that contains an
# ordered collection of objects

a = [0, 0, 0, 0, 0] # list that comprises five plain integers(all zero) and assign it to the variable a

# A list in Python is a dynamic array that stores references to objects
# Each element in the list is a reference(or pointer) to an object in memory

# When we create a list, Python allocates memory for the list itself (ro store the references)
# and for the objects it contains.

# in a = [0, 0, 0, 0, 0] python allocates 
#     memory for the list object(to store 5 references)
#     memory for the integer objects (in this case, the integer 0)
    
#they will have the same address
print(id(a[0]))
print(id(a[1]))

a = [0, 1, 0, 0, 0]

print(id(a[0]))
print(id(a[1]))

# When we call a list/dictionaries we allocate space to each object even if the have the same "value"
# That can be use to ensure to allocate diferent addresses in the memory

b = [[1], [1], [1], [1], [1]]

print(id(b[0]))
print(id(b[1]))
print(id(b[2]))
print(id(b[3]))

#To calculate memory usage of a list we can use getsizeof()
import sys

print(sys.getsizeof(a)) #104
# calculation:
#   For a list, the overhead is typically around 56bytes on a 64-bits system
#   Each element in the list is a pointer/reference to an object in memory
#   On a 64-bits system, a pointer occupies 8Bytes
#   For a list with 5 elements, 5 * 8 = 40 bytes
#       56 + 40 = 96 bytes; 104 should be consider due to additional alignment or internal bookkeping

print(sys.getsizeof(a[0]))

print(a.__len__()) #__len__ build-in function that return the length of ony object

#__init__ method creates list of the desired length and then sets the _baseIndex

class Array(object):
    
    def __init__(self, length = 0, baseIndex = 0): #3 arguments that gives the desired array length and the baseIndex gives the lower bound for array indices.
        assert length >= 0
        self._data = [None for i in range(length)]
        self._baseIndex = baseIndex
        #the defult base index is zero and the default array length is zero

#In Python, when a list is alocted, two things happenn
#   First, memory is allocated for the list object and its elements
#   Second, each element of the list is initialized with the appropriate default value(in this case all of the list elements refer to the None object)

#__copy__ method provides a way to create a copy of a given array. This method creates a shallow copy. A shallow copy of the Array object but dows not copy the objects contained in the array

    def __copy__(self):
        result = Array(len(self._data))
        for i, datum in enumerate(self._data):
            result._data[i] = datum
        result._baseIndex = self._baseIndex
        return result
    
#__getitem__ and __setitem__ methods 
    def getOffset(self, index):
        offset = index - self._baseIndex
        if offset < 0 or offset >= len(self._data):
            raise IndexError
        return offset
    
    def __getitem__(self, index):
        return self._data[self.getOffset(index)]
    def __setitem__(self, index, value):
        self._data[self.getOffset(index)] = value
        
#Both __getitem__ and __setitem__ invoke the getOffset method to translate the given index by subtracting from i the value of the _baseIndex insance attribute. 
        
#Arrays in python
# a collection of elements stored in contiguous memory locations.
# arrays are often represented using lists. Lists are dynamic, so they can grow
# or shrink in size

arr = [1, 2, 3, 4, 5]

#acess
print(arr[0])
print(arr[-1])

#modifying elements
arr[0] = 10
print(arr)

#add element
arr.append(6)
print(arr)

#removing elements
arr.pop()
print(arr)

#its a list but the methods used its array kind
# Common array techniques

#1)- Two Pointer Technique
# is used when you need to solve problems where you need to traverse
# an array from both ends or with two indices. Its often used in problems involvingg sorted arrays or subarrays

def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

arr01 = [2, 7, 11, 15]
target = 9
print(two_sum_sorted(arr01, target))

#2)- Sliding Window
# the sliding window technique is used to solve problems involving subarrays or substrings
# with a fixed or dynamic window size. its efficient because it avoids recalculating results for overlapping windows

#Find the contiguous subarray with the largest sum
def max_subarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr: 
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
arr02 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(arr02))