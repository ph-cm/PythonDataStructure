# A name is a reference to an object, and you can rebind a name to a different object

a = 10 #a is bound to an integer object with value 10
b = a #b is now bound to the same object as 'a'
a = 20 #a is now rebound to a new integer object with value 20

print(a) #20
print(b) #10 (is still bound to the original object)

#Biding in Python has a close relate to how pointers work in lower-level languages like c.
# But python abstracts away the explicit
# use of pointers, making it easier to work with. Here the explanation:
    # The variable 'a' points to the address that 10 was stored
    # than, 'b' points to the same address of 'a', when 'a' starts pointing 
    # to another value, its pointing to other address of the memory but 'b' is still pointing to the old address
    
#Key points:
    # variables are references to an object in  memory
    # Objects lives in memory (and variables point to these object)
    # Rebinding is changing the address pointed by the variable
