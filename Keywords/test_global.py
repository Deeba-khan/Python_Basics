#global
#'global' is a keyword use to declare global variable.

#Accessing global inside function
x = 7 #global variable (by default)
def add():
    print("Prints the global variable that is outside the add(): ", x)
add()

#Modifying Global variable inside a function using "global" keyword
a = 10
def modifying():
    global a #using a 'global' keyword inside a function to modify 'a' value
    a = a + 2 #incrementing value by 2
    print("Modified a global variable 'a' inside a modifying() function: ", a)
modifying()

#Global using in nested function
def mylocal():
    myname = "deeba" #local variable

    def myglobal():
        global myname
        myname = "Broken"
    print("Before calling myglobal(): ", myname)
    myglobal()
    print("After calling myglobal(): ", myname)
    #Before and After calling 'myglobal()' function the variable 'myname' has no effect it takes the value of local variable i.e. 'deeba'

mylocal()
#Outside 'mylocal()' variable takes the value defined in the myglobal() i.e. 'Broken', 
#Because we used the 'global' keyowrd in 'myglobal()' function (local scope).
print("Prints outside the mylocal() main function: ", myname)

#NOTE: Whatever changes we make inside local scope i.e. 'myglobal()' function, it appears outside the local scope i.e.'mylocal()' function