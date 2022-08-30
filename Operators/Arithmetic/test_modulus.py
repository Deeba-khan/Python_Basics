#Modulus is a arithmetic operator.
# "%" operators use to perform modulus
#It is used to find the remainder when first operand is divided by the second.

#Finding remainder of two values by using modulus operator 

val1 = 3 #val1 and val2 are operands
val2 = 2
modulo1 = val1 % val2 #using modulus "%" operator
print("Modulus of {} and {} is {}".format(val1, val2, modulo1))


val3 = 4   
val4 = 4
modulo2 = val3 % val4
print("Modulus of {} and {} is {}".format(val3, val4, modulo2))

val5 = 2
val6 = 5
modulo3 = val5 % val6
print("Modulus of {} and {} is {}".format(val5, val6, modulo3)) #If val1 is smaller then val2 than remainder always be a "val1"

'''val7 = 2
val8 = 0
modulo4 = val7 % val8
print("Modulus of {} and {} is {}".format(val7, val8, modulo4))''' #Return zero divsion error