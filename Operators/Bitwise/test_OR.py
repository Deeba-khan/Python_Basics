#Bitwise OR - "|"
#Bitwise OR works only on integer, first it convert the integer into binary format then performs bitwise OR(bit by bit)calculation. 

#NOTE: OR bitwise Returns 1 if either one of bits is 1, else 0
#NOTE: OR bitwise returns True if either one of is True, else False
a = 10 #[1010]
b = 5  #[101]
print("Perfroms bitwise OR calculation: ", a | b) #[1010 | 101 = 1111] 1111 is binary representation of 15

c = True
d = True
print("Perfroms bitwise OR calculation: ", c | d)

e = True
f = False
print("Perfroms bitwise OR calculation: ", e | f)

g = False
h = False
print("Perfroms bitwise OR calculation: ", g | h)