#except
#'except' is a keyword, it always works with 'try' block. 
# In try.. except block of code, it checks the try block of code, if 'try' has any error than it execute the 'except' block of code.
#except block is use to handle error

x = 2
try:
   x > 5 
except:
    print("Something went wrong!") 
else:
    print("try block executed without raising an error")

#Defining except block with different errors
try:
    z = 8/0
except NameError:
    print("Name error")
except ZeroDivisionError:
    print("Number is dividing by Zero")