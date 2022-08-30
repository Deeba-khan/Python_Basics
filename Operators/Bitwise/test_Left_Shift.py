#Left Shift -  "<<"
#Bitwise left shift works with integer, it shifts the bits to left side. And fills the empty right side space with Zero.
#In left shift doesn't matter value is -ve or +ve it fills the space with Zero at right side

a = 10
leftShift1 = a << 1 #Shift value 10 by 1 bit, it shifts the binary of 10 to left side, and fills the right space with 0
print("Performs bitwise Left Shift '<<': ", leftShift1)

b = 20
leftShift2 = b << 1 #Shift value 20 by 1 bits, it shifts the binary of 20 to left side, and fills the right space with 0
print("Performs bitwise Left Shift '<<': ", leftShift2)

c = -20
leftShift3 = b << 2 #Shift value -20 by 2 bits, it shifts the binary of -20 to left side, and fills the right space with 0
print("Performs bitwise Left Shift '<<': ", leftShift3)
