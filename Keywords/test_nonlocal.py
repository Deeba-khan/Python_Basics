#Nonlocal
#'Nonlocal' is a keyword, used to defined a nonlocal variable, it used inside a "nested function".
#Nonlocal variable 'local scope' is not defined, means that variable neither be in local scope nor in the global scope.

def name():
    x = "Hench guy" #local variable

    def nonname():
        nonlocal x
        x = "Goblin"
        print("Prints x inside the nonname(): ", x) #It returns 'Goblin' cause it's inside 'nanname()' function
    nonname()
    #After calling a 'nonname()' function, below print statment returns 'Goblin' cause we used 'nonlocal' keyword inside 'nonname()'
    print("Prints x outside the nonname(): ", x)
name()

#NOTE: Whatever changes we make to nonlocal variable the changes appears in the local varibale