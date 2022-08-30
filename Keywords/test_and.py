#and
#'and' is a keyword and logical operator is used to combined conditional statement. 
#It returns True if both statement are True, else False

a = 5
andKeyword = a < 10 and a > 3
print("Performs 'and' keyword: ", andKeyword)

#Using and with if statement
a = 10
if a >= 10 and a < 11:
    print("Both statements are True")
else:
    print("One of the statement or both statement is wrong")