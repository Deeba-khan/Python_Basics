#Floor division is a arithmetic operator
# "//" operators use to divide values

#In "Floor Division" Division part divides the first operand by second operand, but the floor fuction see the operands are int, float or both and, 
#print output according to it

#The number come after decimal for eg(2.5) then floor decimal convert the .5 into zero and return 2.0 or just 2

#Floor Division two values

val1 = 3 #val1 and val2 are operands
val2 = 2
floordivision1 = val1 // val2 #using floor division "//" operator
print("Floor Division of {} and {} is {}".format(val1, val2, floordivision1)) #Both values are in interger that's why output come in interger


val3 = 5 
val4 = 3.5
floordivision2 = val3 // val4
print("Floor Division of {} and {} is {}".format(val3, val4, floordivision2)) #[5/3.5 = 1.66666666], floor convert this ".66666666" into Zero. so the output we'll be 1.0
#Here one value is int "5" and another is float "3.5". Floor division always give priority to float value,
#that's why the output come in float.


print("Division of 9 and 2 is: ", 9/2) #If we simply divide it then we get 4.5

#But when we divide the same number but we do floor division, 
#then it'll convert all the number to zero which come after decimal, so answer should be 4.0, but since both values is interger, it print output in integer
val5 = 9
val6 = 2
floordivision3 = val5 // val6
print("Floor Division of {} and {} is {}".format(val5, val6, floordivision3))

#here it'll print 4.0 cause one value is float and another is int
val7 = 9.0
val8 = 2
floordivision4 = val7 // val8
print("Floor Division of {} and {} is {}".format(val7, val8, floordivision4))
