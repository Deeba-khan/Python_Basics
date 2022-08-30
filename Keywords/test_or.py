#or
#'or' is a keyword, it returns True if one of the condition/statment is True, othrwise False
#And 'or' is logical operator

a = 3
b = 6
orKeyword = a > b or a < b #False or True --> True
print("Performs 'or' keyword: ", orKeyword)

c = 6
d = 6
orKeyword1 = c > d or c < c #False or False --> False
print("Performs 'or' keyword: ", orKeyword1)

print("Perfoms 'or' keyword with 'if else' statements: ")
if c <= d or c>d:
    print("One of the conditions is True")
else:
    print("Both conditons is False")