#return
#'return' is a keyword, used to exit a function and return value
#'returns' the value(value expression following the return keyword)
#NOTE: 'retrun' statement cannot be used outside of the function
#NOTE: Statement after 'return' will not be executed

def add():
    a = 4 + 5
    print("Performs 'return' keyword '4+5': ")
    return a
print(add())

def after():
    x = 4**2
    print("Performs 'return' keyword '4**5': ")
    return x
    print("5 is power of 4") #Statement after 'return' will not be executed
print(after())