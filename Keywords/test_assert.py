#assert
#'assert' is a keyowrd used for debugging the code. Means if code returns True or has no error, then nothing will happens. But if code returns False or has error than AssertionError is raised.
#We can print error message, seprated by comma.

x = "Hello"
assert x == "Hello"
print("Code returns True, AssertionError won't raise")

assert x != "Python" #Condition returns True, nothing won't happens

#If conditions returns False, AssertionError raise
#Printing message with assertion error "seprating by comma"
assert x == "Python", "x should be 'Hello'" 
