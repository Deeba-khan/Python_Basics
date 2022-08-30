#del
#'del' is a keyword, it used to delete objects such as list, tuple, whole function, class, item from list, tuple and etc.

list1 = ["apple", "banana"]
del list1[1]
print("Deletes the item from list by using 'del' keyword: ", list1)

class Myclass():
    broken = True
del Myclass
print("Deletes the class 'Myclass' successfully by using 'del' keyword")