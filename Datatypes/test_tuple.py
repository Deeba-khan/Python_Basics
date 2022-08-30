#Sequence Datatype - Tuple()

#Tuple are use store data in one varible, tuple is ordered, allow duplicates and unchangable
#unchangeble means we cannot change, add, remove item after creating a tuple
#To create a tuple use () round brackets

#creating a tuple
tuple_1 = ("apple", "banana", "cherry", "palm")
print("Prints a tuple: ", tuple_1)
print("------------------Tuple_1---------------------")

#Allow dublicates
tuple_2 = ("apple", "banana", "cherry", "banana")
print("Prints a tuple with duplicates", tuple_2)
print("------------------Tuple_2---------------------")

#Length of the tuple
#To know the length of the tuple use "len()" keyword
tuple_3 = ("apple", "banana", "cherry", "watermelon", "muskmelon")
print("Finds a length of the tuple: ", len(tuple_3))
print("------------------Tuple_3---------------------")

#Create a tuple with ONE item
tuple_4 = ("India",) #NOTE: To create a One item tuple, then we have to add "comma" after the item
print("Creates a tuple with single item: ", tuple_4)
print("------------------Tuple_4---------------------")

#Can store different Datatypes in tuple
tuple_5 = ("Apple", 123, True)
print("Creates a tuple with different datatypes: ", tuple_5)
print("------------------Tuple_5---------------------")

#Tuple constructor
#To construct a tuple use "tuple()"
tuple_6 = tuple(("apple, fig", "cherry")) #Note a double brackets
print("creates a tuple by using 'tuple()' constructor", tuple_6)
print("------------------Tuple_6---------------------")

#Accessing item by specifying index number, by using [] 
tuple_7 = ("jim", "gym", "geem", "jeem")
print("Access item from tuple by specified index no.: ", tuple_7[2])
print("Access item from tuple by specified index no.: ", tuple_7[-3])
print("------------------Tuple_7---------------------")

#Range of index, means accessing item by range of index
tuple_8 = ("garden", "flowers", "tree", "plants", "grass", "soil", "slides", "swings","kids")
#starting from 2nd index and ending one step before "stop" range
print("Access item from tuple by specified range of index no.: ", tuple_8[2:9]) #[start: stop: step]
print("Access item from tuple by specified range of index no.: ", tuple_8[-5:-2]) #accessing item by negative index number
print("------------------Tuple_8---------------------")

#check if the item is present in tuple or not
tuple_9 = ("garden", "flowers", "tree", "plants", "grass", "soil", "slides", )
for x in tuple_9:
    if "flowers" in x:
        print("Checks the 'flower' is present in the tuple or not: ", "Yes, it's present")
print("------------------Tuple_9---------------------")

#Update a tuple
tuple_10 = ("numbers", "rational no.", "irrational no.")
#to update a tuple, first we have to convert it into a list, update a list, then convert back into a tuple
updateTuple= list(tuple_10) #converting into a list
updateTuple[1] = "roman number"  #update a list
tuple_10 = tuple(updateTuple)  #converting back into a tuple
print("Updates a tuple: ", tuple_10)
print("------------------Tuple_10---------------------")

#Add item in 
tuple_11 = ("apple", "banana")
#to add tuple in tuple, first we have to convert it into a list, add item in a tuple, then convert back list into a tuple
addItem = list(tuple_11) 
addItem = ("orange",)  #NOTE: Dont forgot to add comma after making a single item tuple, else python won't recognize it's tuple
tuple_11 += addItem
print("Adds item in the tuple: ", tuple_11)
print("------------------Tuple_11---------------------")

#remove item
#since tuple is unchangeable, so, we've to convert tuple into a list, remove item from a list, then convert back into a tuple
tuple_12 = ("banana", "fig", "cherry", "melon")
removeTuple = list(tuple_12)
removeTuple.remove("melon")
tuple_12 = tuple(removeTuple)
print("removes item from the tuple: ", tuple_12)
print("------------------Tuple_12---------------------")

#delete tuple
#you can simply delete the whole tuple by using "del" keyword
tuple_13 = ("banana", "fig", "cherry", "melon")
del tuple_13
#print(tuple_13) #this will raise an error
print("tuple deleted succesfully by using 'del' keyword")
print("------------------Tuple_13---------------------")

#Unpacking the tuple
#usually when we assign a value in tuple known as "packing" a tuple
tuplePacking = ("a", "b", "c", "d") #packing a tuple

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
tuple_14 = ("apple", "banana", "cherry", "palm")
(green, yellow, red, blue) = tuple_14 #variables "this is the way to write" for extracking the value into varibles
#NOTE: The number of varible should be same to number of strings/values in tuple
print("Extracking the value into varibles(unpacking): ", green)
print("Extracking the value into varibles(unpacking): ", yellow)
print("Extracking the value into varibles(unpacking): ", red)
print("Extracking the value into varibles(unpacking): ", blue)
print("------------------Tuple_14---------------------")

#using Asterisk "*"
#if number of varibale is less than number of values is tuple then you can use "*"
tuple_15 = ("apple", "banana", "cherry", "palm")
(a, b ,*c) = tuple_15  #asterisk variable return a list of values
print("Unpacks the tuple, using asterisk variable(a,b,*c)asterisk return a list of values: ", a, b, c) 

(a, *b, c) = tuple_15
print("Unpacks the tuple, using asterisk variable(a,*b,c)asterisk return a list of values: ", a, b, c)

(*a, b, c) = tuple_15
print("Unpacks the tuple, using asterisk variable(*a,b,c)asterisk return a list of values: ", a, b, c)
print("------------------Tuple_15---------------------")

#Loop a tuple
#iterate through a item of tuple
tuple_16 = ("apple", "banana", "cherry", "palm", "melon")
print("Iterate through a item of tuple by using 'for' loop:")
for a in tuple_16:
    print(a)
print("------------------Tuple_16---------------------")

#Loop through the index number
tuple_17 = ("a", "e", "i", "o", "u")
print("Loop through the index number:")
for i in range(len(tuple_17)):
    print(i) #printing index number
print("------------------Tuple_17---------------------")

#using while loop
tuple_18 = ("apple", "banana", "cherry", "palm", "melon")
i = 0
print("Uses 'while' loop: ")
while i <len(tuple_18):
    print(i) #if print i than it return index number of the items
    print(tuple_18[i]) #if print this than it iterate through the item of the tuple
    i += 1
print("------------------Tuple_18---------------------")

#Join tuple
#u can use "+" to join tuple
tuple_19 = ("apple", "banana")
add19 = ("fig", "cherry")
addTuple = tuple_19 + add19
print("joins the tuple by using '+' opreator: ", addTuple)
print("------------------Tuple_19---------------------")

#using "*" opreator to add how many time item should add in tuple
tuple_20 = ("apple", "banana", "fig")
addItem = tuple_20 * 3
print("uses '*' opreator to add how many times item should add in tuple: ", addItem)
print("------------------Tuple_20---------------------")

#Tuple method
#count()
#count method count the how many times specified item appears in the tuple
tuple_21 = ("apple", "banana", "fig", "melon")
countTuple = tuple_21.count("banana")
print(".count('banana') counts how many time 'banana' appears in the tuple: ", countTuple)
print("------------------Tuple_21---------------------")

#index()
#index method return the index number of the specified item, if not found return an error
tuple_22 = ("apple", "banana", "fig")
indexTuple = tuple_22.index("apple")
print(".index('apple') return a index no. of specified item, if not found raise an error: ", indexTuple)
print("------------------Tuple_22---------------------")























































































