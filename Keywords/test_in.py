#in
#'in' is a keyword, it has two purpose
#First, it used to check that specified value is present or not like in list, tuple, string and etc
#Second, it use in 'for' loop to iterate through a sequence collection

mylist = ["chp", "hench guy", "professor", "goblin"]
if "hench guy" in mylist:
    print("Yes, 'hench guy' is present in mylist")

print("Uses 'in' keyowrd to iterate through a tuple in a 'for' loop: ")
mytuple = ("chp", "hench guy", "professor", "goblin")
for i in mytuple:
    print(i)