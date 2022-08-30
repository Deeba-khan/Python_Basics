#import
#'import' is a keyword, used to import module


import datetime
x = datetime.date(year=2002, month=4, day=2)
print("Prints year, month and day: ", x)

#importing 'pi' as variable form 'math' module
from math import pi
print("Prints pi value by importing 'pi' as variables from 'math' module: ", pi)

from math import * 
#By using '*' it imports all the function and constant from the 'math' module
print("Prints factorial of 6: ", factorial(6))
print("Uses 'pow' function from the 'math' module: ", pow(4, 2))