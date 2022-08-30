#Bitwise AND - "&"
#Bitwise AND works only on integer, first it convert the integer into binary format then performs bitwise AND(bit by bit)calculation. 

#NOTE: AND bitwise Returns 1 if both bits is 1, else 0
#NOTE: AND bitwise returns True if both is True, else False
a = 10 #[1010]
b = 5  #[101]
print("Perfroms bitwise AND calculation: ", a & b) #[1010 & 101 = 0000] 

c = True
d = True
print("Perfroms bitwise AND calculation: ", c & d)

e = True
f = False
print("Perfroms bitwise AND calculation: ", e & f)