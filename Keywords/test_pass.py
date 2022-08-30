#pass
#'pass' is a keyword, it works like a future placeholder in the code. Means you add code later...
#When 'pass' statement is executed nothing happens, but it avoid getting error when 'empty code' is not allowed
#Empty code not allowed in loops, functions definition, class definition or in conditional statements(if else).

#Using 'pass' keyword in function
def random():
    pass   #Nothing we happens

#Using 'pass' keyword in class
class henchguy():
    pass  #Nothing we happens

#Using 'pass' keyword in 'if' conditional statement
a = 30
b = 40
if a < b:
    pass  #Nothing we happens

#Using 'pass' statement where it executed
print("Performs 'pass' keyword in conditional statement(if else): ")
c = 50
d = 100
if c > d:
    pass
else:
    print("d is greater than be")

#Using 'pass' in loop and conditional statement
print("Performs 'pass' keyword in 'for' loop and conditional statement(if else): ")
mylist = ["her", "broken", "19"]
for i in mylist:
    if i == "19":
        pass #When i value is equal to 19 then pass the if condition 
    else:
        print(i)