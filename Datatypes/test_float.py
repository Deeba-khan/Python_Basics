#Numeric Datatype - float()
#float return the "float_point number" from a number or specified float-numeric string
#float can work with arithmetic operations

#printing a float
float_1 = float(5)
print("Prints a float: ", float_1)
print("Prints a type: ", type(float_1))
print("------------------float_1---------------------")

#numeric-string to float
float_2 = float("23.1")
print("Converts a numeric-string into float: ", float_2)
print("------------------float_2---------------------")

#converting int into float
int = 999
float_3 = float(int)
print("Converts int into float: ", float_3)
print("------------------float_3---------------------")

#float for "inf" (infinity)
#inf is extremly very large number which has no end
#whereas "-inf" is smallest which is not even equal to zero
#inf is case insensitive and we can compare it
float_4 = float("inf")
print("Prints a 'inf': ", float_4)
print("Prints a 'iNfInITy': ", float("iNfInITy")) #doesn't matter how u write inf it always written "inf" in console
print("Prints a -infIniTy: ", float("-infIniTy")) 
print("------------------float_4---------------------")

#float for "nan" (Not a Number)
# "nan" is something which is undefined, we cannot compare it with anything, it's meaningless (like in math "sqrt(-1)", or 0/0 are undefined, so in computer system "nan" represent that)
#"nan" is case insensitive
#NOTE: Keep in mind that, each time we write float("nan"), 
#it instantaneously changes its value. It will never be equal to another float("nan").
float_5 = float("nan")
print("Prints a nan: ", float_5)
print("Prints a NaN: ", float("NaN"))
print("Prints a naN: ", float("naN"))
print("------------------float_5---------------------")

#converting float into complex
float_6 = 33.8
complex_6 = complex(float_6)
print("Converts float into complex: ", complex_6)