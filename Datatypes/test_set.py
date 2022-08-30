#Sequence Datatype - setss{}

#set is use to store collection of data in one variables
#set is unchangeable, unordered, and unindexed
#unordered means items will appear in random order

#to create set use "{}" curly brackets

#Creating a set
set_1 = {"apple", "banana", "cherry"}
print("Prints a set: ", set_1)
print("------------------Set_1---------------------")

#Duplicate are not allowed
set_2 = {"apple", "cherry", "banana",  "apple"}
print("Prints a set with duplicates values: ", set_2, "(set don't allow duplicates)")
print("------------------Set_2---------------------")

#Find the lenght of the set
set_3 = {"apple", "fig", "melon", "orange"}
print("Finds a length of set: ", len(set_3))
print("------------------Set_3---------------------")

#Can store different type of data in set
set_4 = {"apple", 123, True}
print("Creates a set with different datatypes: ", set_4)
print("------------------Set_4---------------------")

#Find a type
set_5 = {"apple", "melon", "fig", "cherry"}
print("Prints a type: ", type(set_5))
print("------------------Set_5---------------------")

#set constructor
#Use set() to create a set
set_6 = set(("apple", "banana", "fig"))
print("Creates a set by using a set() constructor: ", set_6)
print("------------------Set_6---------------------")

#Acces item
#Since, set is unordered so we cannot access item by index no. Instead we have to loop through the set by using "for" loop
#or we can use "in" keyword to see whether the specified item is present or not, if yes return True, otherwise False
set_7 = {"apple", "banana", "melon", "fig"}
print("Since set is unordered so we loops through the set to get the set items: ")
for i in set_7:
    print(i)

print("Return True if 'fig' is present, else False:  ", "fig" in set_7) #using "in" to see if the item is present or not
print("Return True if 'cherry' is present, else False:  ","cherry" in set_7)
print("------------------Set_7---------------------")

#Change item
#Since, set is unchaneable so, we can add item in set by using .add() method
set_8 = {"apple", "banana", "orange"}
set_8.add("melon")
print(".add('melon') adds the item in set: ", set_8)
print("------------------Set_8---------------------")

#Update set
#To add another set item in the original/current set use .update() method
set_9 = {"melon", "fig", "palm"}
set9_1 = {"apple", "banana"}
set_9.update(set9_1)
print(".update() updates/adds the set in the current set: ", set_9)
mylist = ["veggies"]
set_9.update(mylist) #update method can add not only set but it can add tuple, dictionary, list etc.
print("adds a list to current set by using .update(): ", set_9 )
print("------------------Set_9---------------------")

#remove item
#if item does not exist, remove method raise an error
set_10 = {"life", "hardership", "patience", "time", "easy"}
set_10.remove("easy")
print(".remove('easy') removes 'easy' from the set, if not found raise an error: ", set_10)
print("------------------Set_10---------------------")

#discard item
#if item is not present then discard method won't raise and error
set_11 = {"life", "hardership", "patience", "time", "easy"}
set_11.discard("life")
print(".discard('life') discards the 'life' from set, if not found it won't raise an error: ", set_11)
print("------------------Set_11---------------------")

#pop item
#NOTE: set are unorderd, and pop remove the last item so, you dont know which gets removed from the set
set_12 = {"funny", "crying", "happy", "shocked"}
set_12.pop() 
print(".pop() removes the item from set: ", set_12)
print("------------------Set_12---------------------")

#clear set
#clear method clear the item present in the set, and return empty set
set_13 = {"apple", "fig"}
set_13.clear()
print(".clear() the content from the set and return empty set: ", set_13)
print("------------------Set_13---------------------")

#del set
#del() method use to delete whole set
set_14 = {"fig", "melon", "orange"}
del set_14
#print(set_14) #this will raise an error cause the set does not exits anymore
print("Uses 'del' keyword to deletes the set_14", "[Sucessfully set deleted!]")
print("------------------Set_14---------------------")

#Loop item
#use "for" loop to loop through the items present in the set
set_15 = {1, 2, 3, 4, 5, 6}
print("Loop through a set items: ")
for i in set_15: #loop through the set and print values
    print(i)
print("------------------Set_15---------------------")

#join two sets
#there're several methods to join two set

#union()
set_16 = {"apple", "banana"}
join16 = {"fig", "melon", "apple"}
newSet16 = set_16.union(join16) #union method exculde the duplicate value. NOTE: you have to create a new set "newSet16" to join sets 
print(".union() joins the set and returns a newset and exclude duplicate: ", newSet16) 
print("------------------Set_16---------------------")

#update()
#update method is also use to join two sets
set_17 = {1, 2, 3, 4, 5}
updateSet = {"apple", "apple"} 
set_17.update(updateSet) #updates method exculde the duplicate value.
print("Uses .update() to join sets: ", set_17)
print("------------------Set_17---------------------")

#intersection_update()
#intersection_update() method return ONLY item which are present in both set
set_18 = {"tired", "unhappy", "sad", "crying"}
set18 = {"crying", "sad"}
set_18.intersection_update(set18)
print(".intersection_update() retruns a set of item which present in both sets: ", set_18)
print("------------------Set_18---------------------")

#intersection()
#intersection methon retrun a NEW set, it contains item which are exits in both sets
set_19 = {"hii", "hello", "bye"}
set19 = {"bye"}
newSet19 = set_19.intersection(set19)
print(".intersection() retruns a New set of item which present in both sets: ", newSet19)
print("------------------Set_19---------------------")

#symmetric_difference_update()
#symmetric_difference_update() keep the values that are not present in both set, and skip the value which are present in both set
set_20 = {"microsoft", "google", "outlook"}
set20 = {"outlook", "gmail", "yahoo"}
set_20.symmetric_difference_update(set20)
print(".symmetric_difference_update() return a set of items that are not present in both sets: ", set_20)
print("------------------Set_20---------------------")

#symmetric_difference()
#symmetric_difference method return a NEW set, it contains value that are not present in both set
set_21 = {"apple", "cherry", "banana"}
set21 = {"cherry", "melon", "orange"}
newSet21 = set_21.symmetric_difference(set21) #new set
print(".symmetric_difference() return a New set of items that are not present in both sets: ", newSet21)
print("------------------Set_21---------------------")

#isdisjoin()
#isdisjoin method return True, if set_22 item is NOT present in the set22, otherwise False
set_22 = {"apple", "banana"}
set22 = {"cherry", "melon"}
newSet22 = set_22.isdisjoint(set22)
print(".isdisjoint() returns True if set items is not present in another set, else False: ", newSet22)
print("------------------Set_22---------------------")

#issubset()
#issubset method return True, if set_23 all item is present in set23, else False
set_23 = {"apple", "banana"}
set23 = {"cherry", "melon", "apple", "banana"}
newSet23 = set_23.issubset(set23)
print(".issubset() returns True if set all items is present in another set, else False: ", newSet23)
print("------------------Set_23---------------------")

#isuperset()
#issuperset method return True, if set24 all item is present in set_24, else False
set_24 = {"apple", "banana", "cherry", "melon"}
set24 = {"cherry", "apple"}
newSet24 = set_24.issuperset(set24)
print("issuperset() returns True if atleast one item of set is present in another set: ", newSet24)
print("------------------Set_24---------------------")











































































































