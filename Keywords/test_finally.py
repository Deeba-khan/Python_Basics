#finally
#'finally' is keyword, it used in try.. except block. 'finally' block always executed no matter try...except..else raise error or not

x = 2
try:
    x > 5
except:
    print("Something went wrong!")
finally:
    print("finally block always executed")

try:
    x > 5
except TypeError:
    print("Except block executed!")
else:
    print("else block executed")
finally:
    print("Finally executed no matter what")