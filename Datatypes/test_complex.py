#Numeric type - complex()
#complex return "complex number" which has real and imaginary part.
#if no parameter is passed than it return zero

complex_1 = complex()
print("Prints a complex() number without parameter: ", complex_1)
print("--------------complex_1-----------------")

#int to complex
complex_2 = complex(1) #passing only one parameter
print("Prints a complex no. by passing only one parameter as int, complex(1): ", complex_2)
print("Prints a complex no. by passing two one parameters as int, complex(2,3): ", complex(2, 3)) #passing two parameters
print("--------------complex_2-----------------")

#float to complex
complex_3 = complex(33.5)
print("prints a complex no. by passing only one parameter as float, complex(33.5): ", complex_3)
print("Prints a complex no. by passing two parameters as float, complex(34.5,65.4): ", complex(34.5, 65.4)) #passing two parameters
print("--------------complex_3-----------------")

#numeric_string to complex
complex_4 = complex("9")
print("Prints numeric_string '9': ", complex_4)
#print(complex("9", "7")) #if first parameter is string then 2nd parameter should't be pass, it'll raise an error
print("--------------complex_4-----------------")

#printing complex numeric-string
complex_5 = complex("7+3j")
print("Prints a complex numeric_string", complex_5)
print(type(complex_5))
#print(complex("4 + 5j")) #raise error, there should not be space around opretors
print("--------------complex_5-----------------")

#Extract real and imaginary part from complex number
complex_6 = 4-5j
print("Prints a complex number: ", complex_6)
print("Extracting real part from complex number: ", complex_6.real) #use .real to extract real part from complex number
print("Extracting imaginary part from complex number: ", complex_6.imag) #use .imag to extract real part from complex number
print("--------------complex_6-----------------")