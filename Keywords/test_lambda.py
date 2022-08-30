#lambda
#'lambda' is a keyword, used to create small anonymous function, means a function without a name
#NOTE: lambda can have ONLY function like (a+b+c, a*b, a*c)

#SYNTAX: lambda argument : expression

#Defining a funcion which doesn't have name
f = lambda a : a*3  #'f' represent our function
#As we know in python function are object so, here [lambda a : a*3] is a function. 
#So we need to assign our function i.e. 'lambda a : a*3' to someone, in this case it's 'f'
multiplication = f(3)
print("Performs 'lambda' keyword for multiplication operation: ", multiplication)

#Defining a function which will add two numbers
x = lambda a,b,c : a+b+c #NOTE: We can pass many arguments but ONLY have one expression i.e. a+b+c
addition = x(3,5,5)
print("Performs 'lambda' keyword for addition operation: ", addition)