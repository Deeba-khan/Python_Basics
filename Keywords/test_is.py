#is
#'is' is a keyword, it used to test if two variable refer the same object, if yes than returns True, else False
#'is' test returns False if they are not same object, even they're 100% equal

#NOTE: The == operator is used to test if two objects are the same.

x = ["apple", "mango", "cherry"]
y = x
print("Perfroms 'is' keyword: ", x is y)

#Test that they are not same object, but they're equal
a = ["melon", "fig"]
b = ["melon", "fig"]
print("Perfroms 'is' keyword: ", a is b) #Returns False cause they're not same object, even have same content
print("Perfroms '==' operator: ", a == b) #Returns True cause they're equal

num1 = 40
num2 = 40
print("Perfroms 'is' keyword: ", num1 is num2)