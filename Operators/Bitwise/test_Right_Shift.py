#Right Shift -  ">>"
#Bitwise right shift works with integer, it shifts the bits to right side. And fills the empty left side space with Zero, incase value is neagtive then it fills the space with One

a = 10
rightShift1 = a >> 1 #Shift value 10 by 1 bit, it shifts the binary of 10 to right side, and fills the left space with 0
print("Performs bitwise Right Shift '>>': ", rightShift1)

b = 20
rightShift2 = b >> 1 #Shift value 20 by 1 bits, it shifts the binary of 20 to right side, and fills the left space with 0
print("Performs bitwise Right Shift '>>': ", rightShift2)

c = -20
rightShift3 = b >> 2 #Shift value -20 by 2 bits, it shifts the binary of -20 to right side, and fills the left space with 1
print("Performs bitwise Right Shift '>>': ", rightShift3)