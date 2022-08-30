#break
#break is keyword, it used to break out 'for' loop and 'while' loop.

for i in range(10):
    print(i)
    if i > 4: #it stops at 5 cause i should be greater than 4 and 5 is minimum greater than 4 in range 10
        break

print("---while loop---")
i = 0
while i < 9:
    print(i)
    if i >= 5:
        break #break the loop when i value is greater than equal to 5
    i +=1
