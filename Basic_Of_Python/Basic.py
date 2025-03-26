#Operators Ari
#Sum, Sub, Mult, Div

print(10 + 23) #sum
print(10.9 + 23.5)

print(10 - 23) #sub

print(10 * 23) #mult

print(10 / 23) #div -> float
print(10 // 3) #just interger of the division
print(10 % 23) #rest of the division
print()

#----------------------------------------------------------------------------#
#Operators Logics
#true or false opps (boolean)

print(10 < 5)
print(10 > 5)
print(10 <= 5)
print(10 >= 5)
print(10 == 5)
print(10 != 5)
print()

#---------------------------------------------------------------------------
#Variables
#stores values
x = 7
y = 3
nameUser = "Pedro"
idUser = 1234
budgetUser = 12345.12345

print(x == y)
print(x + y)
print()

#----------------------------------------------------------------------------
#Build-in functions
#Native functions in Python https://docs.python.org/pt-br/3.6/library/functions.html
#
# --------------------------------------------------#
# A         |      B            |   C
# abs()     |      bin()        |   callable()
# aiter()   |      bool()       |   chr()
# all()     |      breakpoint() |   classmethod()
# anext()   |      bytearray()  |   compile()
# any()     |      bytes()      |   complex()
# ascii()   |                   |
#---------------------------------------------------#
# D         |      E            |   F
# delattr() |      enumerate()  |   filter()
# dict()    |      eval()       |   float()
# dir()     |      exec()       |   format()
# divmod()  |                   |   frozenset()
#--------------------------------------------------#
# G         |      H            |   I
# getattr() |      hasattr()    |   id()
# globals() |      hash()       |   input()
#           |      help()       |   int()
#           |      hex()        |   isinstance()
#           |                   |   issubclass()
#           |                   |   iter()
#--------------------------------------------------#
# L         |      M            |   N
# len()     |      map()        |   next()
# list()    |      max()        |
# locals()  |      memoryview() |
#           |      min()        |
#---------------------------------------------------#
# O         |      P            |   R
# object()  |      pow()        |   range()
# oct()     |      print()      |   repr()
# open()    |      property()   |   reversed()
# ord()     |                   |   round()
#--------------------------------------------------#
# S         |      T            |   V
# set()     |      tuple()      |   vars()
# setattr() |      type()       |
# slice()   |                   |
# sorted()  |                   |
# staticmethod()                |
# str()     |                   |
# sum()     |                   |
# super()   |                   |
#-----------------------------------------------------#
# Z         |      _            |
# zip()     |      __import__() |
#------------------------------------------------------#

print(abs(-9)) #module
print(abs(15))

print(min(6, 7, 5, 2, 10)) #min value of a senquence

print(max(10, 3, 26, 7, 9)) #max values of a sequence

print(sum([1, 3, 5, 6, 8])) #sum the total value of the lists element

print(pow(2, 3)) 

print("Show a data")

nome = input("Qual seu nome?")
print(" seu nome eh: " , nome)

help(max) #show how the function works



