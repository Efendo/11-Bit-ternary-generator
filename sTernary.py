import random
shell = open('sTernary.txt', 'w') # selects (or creates) the file 'sTernary.txt'
ternary = set() # creates the 'ternary' set
def gen():
   num = '' # initializes the 'num' variable
   for i in range(0, 11): # creates a 11-Bit ternary (base 3) numbers
        num += str(random.randint(0, 2))
   ternary.add(num) # adds the number to the 'ternary' set
   print(str(len(ternary)) + ' ' + num) # prints the length of 'ternary' and the generated ternary number

while len(ternary) < 177147:
    gen()
print(ternary, file=shell) # this prints out the 'ternary' set into the 'sTernary.txt' file
