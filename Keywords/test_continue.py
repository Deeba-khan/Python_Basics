#continue
#'continue' is a keyword, it use to stop the current iteration in a 'for' loop and 'while' loop and continue the next iteration.

for i in range(10):
    if i == 4:
        continue
    print(i)

print("Stop the loop when i is equal to p, and continues the loop from next iteration")
for i in "Python programming":
    if i == "p":
        continue
    print(i)

print("---while loop---")
i = 0
while i < 9:
    i+=1
    if i == 7:
        continue
    print(i)