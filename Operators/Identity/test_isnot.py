#is not
#"is not" is a identity operator, it returns True if object don't share same memory location, else False.
#Returns True is both object is not same, else False

a = 10
b = 11
print("Perfroms identity operator 'is not' on operands: ", a is not b)

c = 3
d = 3
print("Perfroms identity operator 'is not' on operands: ", c is not d)

list1 = ["apple", "mango"]
list2 = ["apple", "mango"]
#Returns True cause list1 and list2 is not same object, even they have same content.
print("Perfroms identity operator 'is not' on list1 and list1: ", list1 is not list2)

#Return False, cause comparison operator just simply compares both side operands
print("Perfroms comparison operator '!=' on list1 and list1: ", list1 != list2)