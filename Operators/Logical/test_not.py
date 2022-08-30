#not
#not is logical operator, it use to reverse the result
#If both bits is same than 0 and if both bits is different than 1

#not True = False
#not False = True
x = 3
notOperator = (not(x > 1)) 
print("Performs NOT operator: ", notOperator)

notOperator1 = (not(x > 1 and x > 5)) #(not(True and False)) = not(False) --> True
print("Performs NOT operator: ", notOperator1)
