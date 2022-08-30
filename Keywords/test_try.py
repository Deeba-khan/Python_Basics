#try
#'try' is a keyword, used in 'try...except' block of code
#if 'try' block code contain error than 'except' block of code raise an error, and if 'try' block of code has no error than nothing won't happen

try:
    4 / 0
except:
    print("'except' block of code executed: Divided by zero")
print("prints 'try...except' don't stop the flow of code even if the 'except' block of code executed")

try:
    4 // 0
except:
    #"Executed 'except' block of code, and specified error by 'raise' keyword"
    raise Exception("Divided by zero")
print("Won't print this statement cause 'raise' stops the control flow of the code") #It will not print