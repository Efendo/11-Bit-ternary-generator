import random
base = set() # creates the 'ternary' set
bitnum = 8

def Base3(number):
   num = '' # initializes the 'num' variable
   for i in range(0, number): # creates ternary (base 3) numbers
        num += str(random.randint(0, 2))
   base.add(num) # adds the number to the 'ternary' set

while len(base) < 3**bitnum:
    Base3(bitnum)
    
ternary = sorted(base)

print(ternary)
