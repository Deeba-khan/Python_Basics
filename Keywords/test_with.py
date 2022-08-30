#with
#'with' is a keyword, used in exception handling(file handling) and makes code more readiable and clear

#File handling
file = open("with_keyword.txt", "w")
file.write("Hello, World")
file.close()
#We can write the above lines of code in much more easier and clear way by using 'with' keyword

#Using 'with' keyword
with open("with_keyword.txt", "w") as file:
    file.write("Broken") #When we use 'with' than we don't need to close the file 'file.close()'