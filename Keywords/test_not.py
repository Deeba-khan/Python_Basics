#not
#'not' is a keyword, used to reverse the result, and it's a logical operator

x = True
print("Peforms 'not' keyword: ", not x)

y = False
print("Peforms 'not' keyword: ", not y)

a = 3
b = 1
c = a > b
if not c:
    print("'a < b' a is less than b")
else:
    print("'a > b' a is greater than b")