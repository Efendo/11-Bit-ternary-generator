# PYCBase README

📦 PYCBase is a module which can generate from 0 - infinite bits custom base numbers (minimum is base2 (binary) and maximum is base10 (decimal))

## 1. installing PYCBase
👉 The download is [here](https://efendo.github.io/PYCBase/PYCBase.py)
## 2. importing PYCBase in python
To use the PYCBModl module in python create a .py file in the same directory as PYCBModl.py
Now in that new .py file import PYCBModl as PYCBase.

## 3. How to use PYCBase
To use PYCBase create an object and specify too parameters first is how many bits you want one number to have and the second one is the Base parameter like this: obj = PYCBase.RBN(8, 2)
PYCBase includes 2 methods first is GenNum() which generates from the initialized PYCBase.RBN(x, y) from above and GenLis() which uses the GenNum() method to generate a list of all specified parameters (in this case its all 8-bits base2 numbers which is 255 numbers)

## 4. Code Example

1 import PYCBase \n
2 \n
3 obj = PYCBase.RBN(int(input('Bits: ')), int(input('Base: '))) \n
4 print(obj.GenLis()) \n
