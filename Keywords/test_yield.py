#yield
#'yield' is a keyword, it retruns output and 'continue', whereas "return" keyword provide output and 'stop'
#'yield' use inside a function and it create generator
#"Generators" are special fucntion that need to be iterated to get values

#NOTE: When we use 'yield' keyword inside a fucntion than that function becomes a "Generator"

#Defining a function with 'yield' keyword
def add():
    yield 4 + 6

#Creating a generator
generator = add()

#Printing a generator, the generator is object in python
print("Prints a generator: ", generator) #It prints generator is object at certain memory location

#Using generator
for i in generator:
    print("Performs 'yield' keyword: ", i)

#Another example
print("---Another Example---")
def foo():
    yield 3
    yield 5
#To print the value of 'foo()' function, we need to iterate it cause we using 'yield' keyword
for a in foo(): #Using 'for' loop to print all the value together
    print("Performs 'yield' keyword: ", a)