#class
#Class is object constrcutor , or 'blueprint' for creating object.

#TO creat a class we use 'class' keyword. And give it a name. For eg: class Myclasss(), 'Myclass' is a name of class.

#Creating a class with property/attribute name x

class Myclass(): 
    x = 5
print("Prints the class: ", Myclass) 

#Creat object
#For creating a class object we use class name

#Created object p1, and printed value x
p1 = Myclass() #Once we created a object of a class is also known as "instantiating of class"
print("Prints the attribute/property from Myclass: ", p1.x)

#The above example are very simple example about class and objects, but they're not work in real life applications. so for that
#We use __init__() function.

#Every class has __init__() fucntion, which always excuted when class is initiated. __init__() function use to assign values to object properties.
#NOTE: The __init__() function is called automatically every time the class is being used to create a new object.

#Creating a class name Person
class Person(): 
    def __init__(self, name, age): #Use __init__() fucntion to assign values name and age.
            self.name = name
            self.age = age #'self' is just a reference parameter to the current class(it can be any name, but it should always be the first parameter of the class) it use to access variables which belong to class.

#Create a object class 'p2'
p2 = Person("chp", 20)
print(p2.name)
print(p2.age)

#Object method
#Method in object is 'function' which belong to object

class Testing():
    def __init__(myobject, name, age): #'myobject' is reference parameter to the current class(changed it self to myobject), which used to access variable belong to class Testing
        myobject.name = name
        myobject.age = age
    
    def myfunction(myobject): #Created Object Method by passing reference parameter 'myobject'
        print("My name is " + myobject.name, "and my age is " + myobject.age)

p3 = Testing("Broken", "19")
p3.myfunction() #executing object method on the p3 class object