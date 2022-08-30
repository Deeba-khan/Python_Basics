#else
#'else' is a keyword, use in conditional statements(if), if previous conditions is false, then try else.
#else catch anything which isn't caught by previous conditions

#We can use else without 'elif'
a = 30
b = 10
if a < b:
    print("a is less than b")
else:
    print("Performs 'else' keyword: ", "a is greater than b")

#Trying else with if and elif
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("Peforms 'else' with conditional statement 'if' and 'elif': ", "a is greater than b") #Previous both conditions were False