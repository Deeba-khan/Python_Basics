#Dictionary use to store data in single variable and values in "key:value" pairs
#Dictionary are changable, ordered and not allow duplicates 

#To create a dictionary use "{}" curly brackets

#Creating a dictionary
dict_1 = {"name" : "Her", "age" : "19", "year": "2022"}
print("Prints a dictonary: ", dict_1)
print("Access a value by specifying keyname: ", dict_1["name"]) #Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print("------------------Dictionary_1---------------------")

#Find length of the list
dict_2 = {"name" : "Her", "age" : "19", "year": "2022"}
print("Prints a length of the dictionary: ", len(dict_2))
print("------------------Dictionary_2---------------------")

#Don't allow duplicate
#dictionary dont allow item with the same key name
dict_3 = {"name" : "Her", "age" : "19", "year": "2022", "year" : "2003"}
print("Creats a dictionary with duplicates values: ", dict_3, "(dict don't allow duplicates!)")
print("------------------Dictionary_3---------------------")

#Dictionary allow all the datatypess such as strings, booleans, int, list
dict_4 = {"name" : "her", "age" : 19, "broken" : True, "colors" : ["black"]}
print("Creats a dictionary with different datatypes: ", dict_4)
print("------------------Dictionary_4---------------------")

#Type
dict_5 = {"name" : "her", "age": 19}
print("Prints a type: ", type(dict_5))
print("------------------Dictionary_5---------------------")

#Accessing item by "key" name
dict_6 = {"name" : "Her", "age" : "19", "year": "1999"}
print("Access value by specified a keyname: ", dict_6["year"]) #we can access item by it's key name, inside square brackets
print("------------------Dictionary_6---------------------")

#get()
#get() method return the item by specifying key name
dict_7 = {"color1" : "black", "color2" : "blue", "flower1" : "rose", "flower2" : "blackrose"}
getItem7 = dict_7.get("flower2")
print(".get('flower') returns the value by specified keyname: ", getItem7) 
print("------------------Dictionary_7---------------------")

#keys()
#keys() method retrun all the keys list present in the dictionary
dict_8 = {"color1" : "black", "color2" : "blue", "flower1" : "hibiscus", "flower2" : "blackrose"}
allKeys8 = dict_8.keys()
print(".key() returns the list of all the keys: ", allKeys8) 
print("------------------Dictionary_8---------------------")

#Adding another key-value pair to see the change in "keys list" after adding separately
dict_9 = {"car" : "BMW", "color" : "Black"}
allkeys9 = dict_9.keys()
print("List of keys before change: ", allkeys9) #before the change

dict_9 ["year"] = 2000 #Adding key value pair
print("List of keys after adding a key separately: ", allkeys9) #after the change
print("------------------Dictionary_9---------------------")

#values()
#values() method return all the value list present in the dictionary
dict_10 = {"car" : "BMW", "color" : "white"}
allvalues10 = dict_10.values()
print(".values() returns the list of all the values: ", allvalues10)
print("------------------Dictionary_10---------------------")

#Adding another key-value pair to see the change in "values list" after adding separately
dict_11 = {"car" : "BMW", "color" : "white"}
allvalues11 = dict_11.values()
print("List of values before change: ", allvalues11) #before the change

dict_11 ["year"] = 2003 #Adding key value pair
print("List of values after adding a value separately: ", allvalues11) #after the change
print("------------------Dictionary_11---------------------")

#items
#items() return all the key value pairs as tuple inside a list
dict_12 = {"name":"her", "age":"19", "color":"black"}
getItem12 = dict_12.items()
print(".items() returns the key-value pairs as tuple inside the list: ", getItem12)
print("------------------Dictionary_12---------------------")

#update a dictionary by making change in original dictionary, and see update key-value list
dict_13 = {"state":"Maharashtra", "country":"India"}
getItems13 = dict_13.items()
print("key-values before update as tuple inside the list: ", getItems13)

dict_13 ["country"] = "Greece" #updating value by using same key name
print("key-values after update as tuple inside the list: ", getItems13)
print("------------------Dictionary_13---------------------")

#Check key is present or not
#Use "in" key word to determine key is present or not
dict_14 = {"state":"Maharashtra", "country":"India", "city":"Mumbai"}
if "city" in dict_14:
    print("Checks 'city' key is present or not: ", "Yes, It's present in the dictionary") #If not then it won't print anything
print("------------------Dictionary_14---------------------")

#Change Values
#change value by using same key name in dictionary
dict_15 = {"name":"him", "age":"19"}
print("Set before change: ", dict_15)
dict_15 ["name"] = "her"
print("Set after changes the value by using same keyname: ",dict_15)
print("------------------Dictionary_15---------------------")

#Update()
#update method the update the original dictionary by giving argument, and argument must be dictionary
dict_16 = {"name":"him", "age":"19"}
print("Before update: ", dict_16)
dict_16.update({"age":"20"}) #NOTE: Give arugument in key-value pair inside curly brackets "dictinary", and use same key name
print(".update({'age':'20'}) updates a set by passing a dicitonary[After update]: ", dict_16)
print("------------------Dictionary_16---------------------")

#Add item
#One simple way to add is use dictionary name, add list of same key name
dict_17 = {"name":"her", "country":"India"}
dict_17 ["age"] = 19
print("Simply adds a key-value pair by using same dicitonary name: ", dict_17)
print("------------------Dictionary_17---------------------")

#update
#by using update() method we can add item in the dictionary
dict_18 = {"name":"her", "country":"India"}
print("Origial dictionary: ", dict_18)
dict_18.update({"color" : "black"}) #passing argument, and argument should be dicitonary
print("Updates a dictionary by passing dict inside .update({'color'':'black'}): ", dict_18)
print("------------------Dictionary_18---------------------")

#Removing item from dictionary by different methods

#pop()
#pop method pop item by specified key name
dict_19 = {"name":"her", "age":"19", "country":"India", "graduate": False}
dict_19.pop("country")
print(".pop('country') pops 'country' from the dicitonary: ", dict_19)
print("------------------Dictionary_19---------------------")

#popitem()
#popitem method remove last item
dict_20 = {"name":"her", "age":"19", "country":"India", "graduate": False}
dict_20.popitem()
print(".popitem() removes a last key-value pair from dictionary: ", dict_20)
print("------------------Dictionary_20---------------------")

#del
#del method delete the specified key name or whole dictionary
dict_21 = {"name":"him", "age":"19", "country":"India", "graduate": False}
del dict_21["name"]
print("'del dict_21['name']' deletes the specified key-value: ", dict_21)
del dict_21
print("deleted whole dictionary by using del keyword")
print("------------------Dictionary_21---------------------")

#clear()
#clear method clear the content and return empty dictionary
dict_22 = {"name":"him", "age":"19", "country":"India", "graduate": False}
dict_22.clear()
print(".clear() clears the content and returns a empty dictionary: ", dict_22)
print("------------------Dictionary_22---------------------")

#Loop dictionary in different ways

#for loop
#loop through the dictionary
dict_23 = {"name":"her", "college":"Thakur", "Degree":"CS"}
print("Loop through a dictionary: ")
for i in dict_23:
    print(i) #printing only key names one by one
    print(dict_23[i]) #printing only values one by one
print("------------------Dictionary_23---------------------")

#using "values()" method  in for loop to get only values one by one
dict_24 = {"car":"Audi", "color":"black", "year":2022}
print("Loop through a dictionary using .values() to get only values one by one: ")
for x in dict_24.values():
    print(x)
print("------------------Dictionary_24---------------------")

#using "keys()" method  in for loop to get only keys one by one
dict_25 = {"car":"Audi", "color":"black", "year":2022}
print("Loop through a dictionary using .keys() to get only keys one by one: ")
for x in dict_25.keys():
    print(x)
print("------------------Dictionary_25---------------------")

#using "items()" method  in for loop to get key_value one by one in tuple
dict_26 = {"car":"Audi", "color":"black", "year":2022}
print("Loop through a dictionary using .items() to get key-value pairs as tuple one by one: ")
for x in dict_26.items():
    print(x)
print("------------------Dictionary_26---------------------")

#copy()
#copy method use to make a copy of dictionary
dict_27 = {"name":"her", "age":"19"}
copydict27 = dict_27.copy()
print(".copy() copies the dictionary: ", copydict27)
print("------------------Dictionary_27---------------------")

#Another method is use dict() function to copy a dictionary
dict_28 = {"numbers":1234}
copydict28 = dict(dict_28) #making a copy of dict by using dict funtion
print("Uses dict() to copy a dictionary: ", copydict28)
print("------------------Dictionary_28---------------------")

#Nested dictionary
#nested dictionary means dictionary contain dictionary
dict_29 = {"child1" : {"name":"her", "age":"19"}, "child2": {"name":"chp", "age":"20"},"child3": {"name":"hench guy", "age":"20"}}
print("Creates a nested dicitonary: ", dict_29)
print("Access dictionary from nested dictionary: ", dict_29["child1"])
print("------------------Dictionary_29---------------------")

#creating three dictionary and adding into ONE new dictionary
child1 = {"name": "Angel", "age":"17"}
child2 = {"name": "Kabir", "age":"7"}
child3 = {"name": "her", "age":"19"}
dict_30 = {"detail1" : child1, "detail2": child2, "detail3" : child3}
print("Creates three dictionary and adding into ONE new dictionary", dict_30)
print("------------------Dictionary_30---------------------")

#fromkeys()
#fromkeys method return a dictionary from specified key-values
keys31 = ["name", "age"] #Doesn't matter you specifying key-values in list, tuple or etc
values31 = ("her", 0)
dict_31 = dict.fromkeys(keys31, values31)
print("'dict.fromkeys(keys31, values31)' return a dictionary: ", dict_31)

#Giving only one argument "keys"
dict_31 = dict.fromkeys(keys31)
print("'dict.fromkeys(keys31)' return a dictionary with None values: ", dict_31)
print("------------------Dictionary_31---------------------")

#setdefault
#setdault meathod return the value by specified key name. and if key does not exit it return none
dict_32 = {"car":"porsche", "color":"red"}
setdict32 = dict_32.setdefault("car")
print(".setdefault('car') returns the value by specified key name: ", setdict32)

setdict32 = dict_32.setdefault("year") #does not exist it'll return none
print(".setdefault('year') returns the value by specified key name, if not found retunrns None: ", setdict32)
print("------------------Dictionary_32---------------------")
