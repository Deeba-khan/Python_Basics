#if
#'if' is a keyword, used in conditional statement, and allow us to execute 'if' block of code only if a condition is True

a = 3
if a == 3:
    print("Executes 'if' block of code cause condition is True") #if conditon would be False then it won't return anything

#'if' block of code condition is not True than, using 'else' block of code to execute code
x = 40
if x == 30:
    print("Executes 'if' block of code, cause x is equal to 40")
else:
    print("Executes 'else' block of code, cause x is not equal to 40")