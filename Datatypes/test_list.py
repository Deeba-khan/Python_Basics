#Sequence datatypes -  list []
#List are ordered, mutable, allow duplicate value, and can create list 1 using "[]"
#List are use to store multiple value in singal varible

#creating a list
list_1 = ["apple", "banana", "mango", "cherry"]
print("Prints a list: ", list_1)
print("------------------List_1---------------------")

#list allow dublicates
list_2 = ["apple", "apple", "watermelon"]
print("Prints a list with dulicate values: ", list_2)
print("------------------List_2---------------------")

#Find a length of list 1 using "len()"
list_3 = ["name", "surname", "fathername", "mothername"]
print("Finds a length of the list: ", len(list_3))
print("------------------List_3---------------------")

#List can store different datatypes
list_4 = ["world", 34, True, False, 100] #storing string, int, boolean values
print("Prints a list with different datarypes: ", list_4)
print("------------------List_4---------------------")

#List constructor 
#create a list by using "list(("add data"))"
list_5 = list(("items", "quantity", "price")) #NOTE: Using double brackets to create a list
print("Creates a list by using list() constructor: ", list_5)
print("------------------List_5---------------------")

#Accesing item by index number, inside [] 
list_6 = ["role", "camera", "action"]
print("Access item from list by index number[2] : ", list_6[2])
print("Access item from list by negative index number[-1]: ", list_6[-1])
print("------------------List_6---------------------")

#Accessing item by giving a range
#in range you can specify where to start and where to end
list_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Access item from list by specified range[2:8]: ", list_7[2:8]) #NOTE: it always stop one step before the end specified index number
print("Access item from list by specified range[:11]: ", list_7[:11]) #deafault start from index 0
print("Access item from list by specified range[3:]: ", list_7[3:]) #range will go to the end 
print("Access item from list by specified negative range[-5:-2]: ", list_7[-5:-2]) #accesing items negative range
print("------------------List_7---------------------")

#Check if item is present in list
list_8 = ["apple", "banana", "mango", "cherry"]
if "cherry" in list_8:  #using "in" keyword to check item
    print("Uses 'in' to check 'cherry' is present in the list or not: ", "Yes, it's present") #if item is not present then it won't print anything
print("------------------List_8---------------------")

#change item in the list
list_9 = ["animals", "bird", "insects"]
list_9[1] = "Trees"
print("Changes item in the list by specified index no.: ", list_9)
print("------------------List_9---------------------")

#change item by range
list_10 = ["mango", "apple", "cherry", "banana", "watermelon", "muskmelon", "palm"]
list_10[2:5] = ["fig", "papaya"] #replacing from 2 to 5 by 2 values (fig, papaya)
print("Changes items from specified range [2:5] by 2 values [fig, papaya]: ", list_10)
list_10[0:3] = ["watermelon"] #replacing from 0 to 3 by 1 value("watermelon")
print("Changes items from specified range [0:3] by 1 values [watermelon]: ", list_10)
print("------------------List_10---------------------")

#insert item to the list
#insert method insert the item at specific index number
list_11 = [1, 2, 3, 4]
list_11.insert(2, "numbers")
print(".insert(2, 'numbers') inserts the item at specific index number: ", list_11)
print("------------------List_11---------------------")

#Add item to the list
#append method add the item at the end of list
list_12 = ["school", "college"]
list_12.append("university")
print(".append('university') adds the item at the end of the list: ", list_12)
print("------------------List_12---------------------")

#extend list
#extend method let's you to add the another list to current list, and extend method add the list or item at the end
list_13 = ["spinch", "potato", "tomato"]
extendList = ["apple", "mango", "cherry"]
list_13.extend(extendList)
print(".extend(extendlist) extends the list into current list at the end: ", list_13)
extendTuple = ("kiwi", "orange", "kiwi") #we can extend any iterable (list, tuple, sets, dict)
list_13.extend(extendTuple)
print(".extend(extendTuple) extends the tuple into current list at the end: ", list_13)
print("------------------List_13---------------------")

#remove item
#remove method remove the specified item
list_14 = ["apple", "mango", "cherry"]
list_14.remove("mango")
print(".remove('mango') removes the 'mango' from the list: ", list_14)
print("------------------List_14---------------------")

#pop item
#pop method remove the item by specified index number, and if index no. isn't specified it remove last item from the list
list_15 = ["a", "b", "c", "d", "e", "f"]
list_15.pop(3)
print(".pop(3) removes the item by specified index no. from the list: ", list_15)
list_15.pop()
print(".pop() removes the last item from the list: ", list_15)
print("------------------List_15---------------------")

#delete item
#del key word use to delete item by specified index no.
list_16 = ["a", "v", "i"]
del list_16[2]
print("'del list_16[2]' deletes the item by specified index no.: ", list_16)
del list_16 #del can delete the whole list
print("'del list_16' deletes the whole list")
print("------------------List_16---------------------")

#clear item
#clear method clear the content from the list, and print the empty list
list_17 = ["c", "h", "p"]
list_17.clear()
print(".clear() clears the content from the list and return empty list: ", list_17)
print("------------------List_17---------------------")

#Loop list
#we can loop through the list by using "for" loop
list_18 = ["h", "e", "n", "c" , "h", "g", "u", "y"]
for a in list_18:   # a is variable which iterate through the list
    print(a)
print("Loop through a list by using 'for' loop")
print("------------------List_18---------------------")

#loop through a list by index number
#rang() and len() we use these function to create suitable iterable
list_19 = ["h", "e", "n", "c" , "h", "g", "u", "y"]
for x in range(len(list_19)):
    print(x)
print("------------------List_19---------------------")

#While loop to loop throught the list
list_20 = ["day", "night", "evening", "dawn"]
i = 0
while i < len(list_20):
    print(i)
    print(list_20[i])
    i = i+1
print("------------------List_20---------------------")

print("-----------List Comprehension examples--------")
#list comprehension
#list comprehension print the list regardless, and with list comprehension we can write code in few lines
list_21 = ["day", "night", "evening", "dawn"]
times = []
for x in list_21:  #without list comprehension we need to use "for" statement
    if "a" in x: #printing a new list which contain "a"
        times.append(x)
print(times)

#In above example we use for loop to create a list
#However we can done this in few lines by list comprehension
# syntax: newlist = [expression for item in iterable if condition == True]
listComprehension_1 = ["apple", "mango", "banana", "cherry", "fig"]
newList_1 = [x for x in listComprehension_1 if "a" in x]
print("Prints a list of only items which contain 'a' in the spellings: ", newList_1)
print("------------------List_21 & newList_1---------------------")

listComprehension_2 = [1, 2, 3, 4, 5]
newList_2 = [x for x in listComprehension_2] #"condition" is optional it can be omitted
print("Loop through a list by list comprehension: ", newList_2)
print("------------------newList_2---------------------")

listComprehension_3 = ["apple", "mango", "banana", "cherry", "fig"]
newList_3 = [x for x in listComprehension_3 if x!= "mango"] #the condition means "if x is not equal to mango then print remaning items except mango"
print("if x is not equal to mango then prints a list of remaining items by list comprehension: ", newList_3)
print("------------------newList_3---------------------")

listComprehension_4 = ["apple", "mango", "banana", "cherry", "watermelon", "cherryyy"]
#"in" keyword see that RHS is inside LHS or not, if yes it returns True, else Flase. 
# But here we printing list, so it'll print all the strings which contain "cherry" inside it
newList_4 = [x for x in listComprehension_4 if "cherry" in x] #List of all strings that have word "cherry" inside it 
print(" 'in' list comprehension: ", newList_4)
print("------------------newList_4_in---------------------")

#"is" keyword is kinda "==" compares LHS and RHS, if same than retruns True, else False
newList_4_1 = [x for x in listComprehension_4 if x is "cherry"]  #List of all strings that are only and only "cherry"
print(" 'is' list comprehension: ", newList_4_1)
print("------------------newList_4_is---------------------")

#range funtion to create an iterables
newList_5 = [x for x in range(10)]
print("Prints a list of range(10) by list comprehension: ", newList_5)
print("------------------newList_5---------------------")

newList_6 = [x for x in range(10) if x < 6] #with condition
print("Prints a list till x is less than 6 by list comprehension", newList_6)
print("------------------newList_6---------------------")

listComprehension_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList_7 = [x if x != 2 else 55 for x in listComprehension_7]
print("Prints a list, if x is not equal to 2 then print remaining item else print 55 by List comprehension: ", newList_7)

#breakdown of above list comprehension
listComprehension_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList_7 = []

for x in listComprehension_7:
    if x != 2: 
        newList_7.append(x)
    else:
        newList_7.append(55)
print("breakdown output: ", newList_7)
print("------------------newList_7---------------------")

#sort the list
#sort method sort the list in the alphanumerically, ascending order, and modfify in-place
list_22 = ["apple", "mango", "banana", "cherry", "watermelon", "fig", "palm"]
list_22.sort()
print(".sort() sorts the list: ", list_22)
sortList22 = list_22.sort() #modified in-place
print(".sort() modified the list in-place: ", list_22) #printing original list instead of "sortList22" because sort method modified in-place
print("------------------List_22---------------------")

#sorting numeric list
list_23 = [355, 66, 12, 10, 3 , 44]
list_23.sort()
print(".sort() sorts the numeric list: ", list_23)
print("------------------List_23_numericSort---------------------")

#sorting the list in descending order
#use key argument "reverse=True" 
list_24 = ["india", "uk", "america", "greece"]
list_24.sort(reverse=True)
print(".sort(reverse=True) sorts the list in descending order: ", list_24)
print("------------------List_24_descending---------------------")

#Case sensitive sort()
list_25 = ["apple", "Banana", "mango", "Fig"]
list_25.sort()
print(".sort() by default sorts the uppercase before lowercase: ", list_25) #by default sort method sort the uppercase string before lowercase letters
print("------------------List_25---------------------")

#so, to make the sort case-sensitive to case-insnsitive use key arg "str.lower"
list_25_1 = ["apple", "Banana", "mango", "Fig"]
list_25_1.sort(key= str.lower)
print("To makes .sort() case-insenitive passed key argument 'str.lower': ", list_25_1)
print("------------------List_25_1---------------------")

#sorted function
#sorted function simply sort the list alphanumerically and in ascending order
list_26 = ["apple", "mango", "fig", "banana"]
sorted_26 = sorted(list_26)
print("sorted() simply sorts the list alphanumerically and in ascending order", sorted_26)
print("------------------List_26---------------------")

#reverse method
#reverse method reverse the list, and modify in-place
list_27 = ["Egg", "Milk", "pancakes", "Butter", "Rusk", "Tea", "Coffe"]
list_27.reverse()
print(".reverse() reverses the list: ", list_27)
reverse_27 = list_27.reverse()
print(".reverse() modefied the list in-place: ",list_27) #modify in-place
print("------------------List_27---------------------")

#reversed function
#reverse function reverse the list
list_28 = ["Egg", "Milk", "pancakes", "Butter", "Rusk", "Tea", "Coffe"]
reversed_28 = list(reversed(list_28)) #simply reversed the list. But note we have to use list() constructor to reserved list.
print("reversed() the list by using list() constructor: ", reversed_28)
print("------------------List_28---------------------")

#copy list
#using "copy()" to copy a list, it simply copy a list
list_29 = ["apple", "egg", "mangos"]
list_29.copy()
print(".copy() copies the list: ", list_29)

#Another method to copy a list is, use "list()" to copy a list
listCopy_29 = ["apple", "egg", "mangos", "fig"]
copyList = list(listCopy_29)
print("copy a list by using list() constructor: ", copyList)
print("------------------List_29---------------------")

#join a list
#There are different ways to join a two list such as, "+" opreator, append(), extend()
list_30 = [8, 0, 11]
join_30 = ["dee", "avi"]
joinList = list_30 + join_30
print("Joins the list by using '+' operator: ", joinList)

#for join a two list by "append()" method we have to use for loop
for x in join_30:
    list_30.append(x)  #appending "join_30" list all items in list_30
print("Joins the list by using append() method: ", list_30)

#join a list by usin .extend() method
joinExtend = list_30.extend(join_30)
print("Joins the list by using extend() method: ", list_30)
print("------------------List_30---------------------")

#count
#count method count how many times item appears in the list
list_31 = [1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
listCount = list_31.count(2)
print(".count(2) counts how many times '2' appears in the list: ", listCount)
print("------------------List_31---------------------")

#index
#index method return the index number of specified value, and if not found it'll raise an error
list_32 = [11, 22, 33, 44, 55, 66, 77, 88, 99, "DK"]
listIndex = list_32.index(11)
print(".index(11) return a index no. of specified item: ", listIndex)
listIndex = list_32.index("DK")
print(".index('DK') return a index no. of specified item, if not found raise an error: ", listIndex)
print("------------------List_32---------------------")

#slicing
#slicing stop one step before end index number
list_33 = [11, 22, 33, 44, 55, 66, 77, 88, 99, "DA"]
print("Slicing a list[:5]", list_33[:5])  #slicing [start: stop: step] 
print("Slicing a list[3:]", list_33[3:])
print("------------------List_33---------------------")





