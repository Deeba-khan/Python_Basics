#Numeric Datatype - int()

#integer are whole number, positive, negative, without decimal, of unlimited length
#Use int() constructor to produce int type integer
#interger can work with arithmetic opreations

#syntax: int(value, base[optional]), 
# "value" means a number or string that can convert into integer.
# "base" means a number representing number format, default is 10

#Printing a type
int_1 = 5
print("Prints a int: ", int_1)
print("Prints a type: ", type(int_1))  
print("------------------int_1---------------------")

#Converting a numeric-string into integer
int_2 = int("1")
print("Converts a numric string into int: ", int_2)
print("------------------int_2---------------------")

#converting float into int
int_3 = 55.8
print("Converts a int into float: ", float(int_3))
print("------------------int_3---------------------")

#int can be negative
int_4 = -45152
print("Prints a negative int: ", int_4)
print("------------------int_4---------------------")

#unlimited length 
int_5 = 41205963159712025489
print("Prints a unlimited length of integer: ", int_5)
print("------------------int_5---------------------")

#converting int into complex 
int_6 = 4
print("Converts a int into complex: ", complex(int_6))
print("------------------int_6---------------------")





