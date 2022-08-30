#is
#Identity operator compares the memory location of the object, from which it's possible to know that object is same or not. 
#"is" returns True if memory location is same, else False
#"is" is the identity operator, returns True if both object is same, else False.

a = 5
b = 5
print("Peforms identity operator 'is' on operands: ", a is b)

list1 = ["apple", "mango"]
list2 = ["apple", "mango"]
#returns False cause list1 is not same object as list2, even if they have same content.
print("Peforms identity operator 'is' on list1 and list2: ", list1 is list2) 

#It returns True cause list1 is equal to list2
print("Peforms comparison operator '==' on list1 and list2: ", list1 == list2) 
