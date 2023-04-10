# 11BIT TERNARY GENERATOR
import random
ternary = []
contains = 0
number = ""
print("ternary generator V1")
print("generation started")
def has():
  contains = 0
  for i in range(len(ternary)):
    if ternary[i] == number:
      contains += 1
  if 0 == contains:
    ternary.append(number)
    print(number)
def Generate():
  global number
  number = ""
  for i in range(11):
    number = number + str(random.randint(0, 2))
  has()
while len(ternary) != 177147:
  Generate()
print("done!")
