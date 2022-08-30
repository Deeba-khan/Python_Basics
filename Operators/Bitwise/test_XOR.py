#Bitwise XOR - "^"
#Bitwise XOR works only on integer, first it convert the integer into binary format then performs bitwise XOR(bit by bit)calculation. 

#NOTE: XOR bitwise Returns 0 if both bits is same, else 1
#NOTE: XOR bitwise returns True if both value is different, else if both value is same XOR returns False
a = 10 #[1010]
b = 5  #[101]
print("Perfroms bitwise XOR calculation: ", a ^ b) #[1010 ^ 101 = 1111] 11111 is binary representation of 15

c = False
d = False
print("Perfroms bitwise XOR calculation: ", c ^ d) 

e = False
f = True
print("Perfroms bitwise XOR calculation: ", e ^ f) 