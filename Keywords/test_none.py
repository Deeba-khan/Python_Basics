#None
#'None' is a keyword, it used to defined a null value, or no value at all
#'None' is not False, True, empty string or 0, None is it's own type(NoneType), None is just None!

x = None
print("Performs 'None' keyword: ", x)

#Boolean test on None value
y = None
if y:
    print("Prints if y 'None' is True")
elif y is False:
    print("Prints if y 'None' is False")
else:
    print("Performs 'None' keyword: ", "'y' value None is not True not False, None is just None..")