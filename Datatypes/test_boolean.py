#Boolean represent "True" or "False"
#You can evaluate any expression in Python, and get one of two answers, True or False.

#Almost values are True, any number, string, list and etc are True

#Comparing two values
a = 1
b = 2
bool_1 = a < b
bool_2 = a == b
bool_3 = a > b
print("Returns booleans value True if a<b, else False: ", bool_1)
print("Returns booleans value True if a==b, else False: ", bool_2)
print("Returns booleans value True if a>b, else False: ", bool_3)
print("------------------Boolean_1, 2 & 3---------------------")

#Evaluate string
bool_4 = "Hello"
print("'Hello' returns True if it's a string, else False: ", bool(bool_4))
print("------------------Boolean_4---------------------")

#Evaluate number
bool_5 = 112345
print("'112345' returns True if it's a number, else False: ", bool(bool_5))
print("------------------Boolean_4---------------------")

#Evaluate list
bool_6 = ["HII"]
print("'[HII]' returns True if it's a list, else False: ", bool(bool_6))
print("------------------Boolean_5---------------------")

#Evaluate tuple
bool_7 = ("hello",)
print("('hello',) returns True if it's a tuple, else False: ", bool(bool_7))
print("------------------Boolean_7---------------------")

#Evaluate set
bool_8 = {"Fine"}
print(" {'Fine'} returns True if it's a set, else False: ", bool(bool_8))
print("------------------Boolean_8---------------------")

#Evaluate dictionary
bool_9 = {"borken" : "Yes"}
print("'{'broken':'Yes'}' return True if it's a dictionary, else False: ", bool(bool_9))
print("------------------Boolean_9---------------------")

#In fact, there are not many values that evaluate to False, 
#except empty values, such as tuple(), list[], set{}, string "", the number 0, and the value None. 
#And of course the value False evaluates to False.

#Evaluate empty string
bool_10 = "" #Any string is True, except empty string
print(" ' ' returns True if it's a string, else False: ", bool(bool_10), "(Any string is True, except empty string)")
print("------------------Boolean_10---------------------")

#Evaluate number zero
bool_11 = 0 #any number is True, except 0
print(" '0' returnsTrue if it's a number, else False: ", bool(bool_11), "(any number is True, except 0)")
print("------------------Boolean_11---------------------")

#Evaluate empty list
bool_12 = [] #any list is True, except empty list
print(" '[]' returns True if it's a list, else False: ", bool(bool_12), "(any list is True, except empty list)")
print("------------------Boolean_12---------------------")

#Evaluate value
bool_13 = None #any values is True, except value None
print("'None' returns True if it's a value, else False: ", bool(bool_13), "(any values is True, except value None)")
print("------------------Boolean_13---------------------")

#Function can return Boolean
def bool_14():
    return True
print("Function returns a True: ", bool_14())
print("------------------Boolean_14---------------------")

#getting a boolean value, by making a condition
def bool_15():
    return True

if bool_15: #It means "if this condition is True" then print yes
    print("YES") 
else:
    print("NO")
print("------------------Boolean_15---------------------")

#If you wanna run "if block" on "false" conditions then u can add a "not" to it.
def bool_16():
    return True

if not bool_16():  #not True means False
    print("NO")
else:
    print("Yes")
    print("------------------Boolean_16---------------------")