#Text datatype -  "str"
#To create a string write anything inside a Single ('') or Double (" ") quotes!

#Printing a string
str_1 = "Hello, World!"
print("Printing a text string: ", str_1)
print("------------------str_1---------------------")

#Number can be a string if its in single or double quotes 
str_2 = '123456789'
print("Printing a numeric string: ", str_2)
print("------------------str_2---------------------")

#Capitalize
#Capitalize a string
str_3 = "code for code"
cap = str_3.capitalize()
print("Capitalize only a first letter of string: ", cap)
print("------------------str_3---------------------")

#upper()
#Uppercase the string
str_4 = "egg"
upper_4 = str_4.upper()
print("Converts a string into uppercase: ", upper_4)
print("------------------str_4---------------------")

#lower()
#Lowercase the string
str_5 = "EGG"
lower_5 = str_5.lower()
print("Converts a string into lowercase: ", lower_5)
print("------------------str_5---------------------")

#casefold()
#casefold convert the character of string into a lowercase
str_6 = "PrograMMING,Coding"
casef = str_6.casefold()
print("Converts a string into casefold: ", casef)
print("------------------str_6---------------------")

#center()
#center method align the string in the "center" and fill up each side (left & right) by default space
'''center method take 2 argument, one is for align the string in center by giving specific charcter (in this case 100), 
and another one is optional, it can be character which fill the "each side" space. '''
str_7 = "singing"
cen = str_7.center(50) #filling each side by space 
print(".center(50) centers the string: ", cen)
cen_1 = str_7.center(30, "A") #provided optional arg "A" to fill the each side space
print(".center(30, 'A') centers the string and filled a space by argument 'A': ", cen_1)
print("------------------str_7---------------------")

#count()
#count method count how many time character or item appears in the string
str_8 = "Python is easy to learn, give it a try!"
str_8_c = str_8.count("a") 
print (".count(a) counts how many times 'a' appears in the string: ", str_8_c)
str_8_c = str_8.count(" ") #counting a space
print (".count(' ') counts how many time 'space' appears in the string: ", str_8_c) 
str_8_c = str_8.count("p") 
print (".count('p') counts how many times 'p' appears in the string: ", str_8_c) #return zero cause python is case sensitive lang 
print("------------------str_8---------------------")

#encode()
#string stored as Unicode, means each character of string is represent by code points, so the string is just a sequence of "Unicode code points"
#and this code points converted into set of bytes, and this is known as "encoding"
#encoding has 2 parameters "encoding", "error"

str_9 = "5"
enc_9 = str_9.encode() #if encode parameter is not specify then it use "utf-8" default parameter for encoding
print("Encodes a string: ", enc_9)
print("------------------str_9---------------------")

#Trying encoding parameters
#There're total 6 errors, it comes when in encoding parameter don't able to encode that char of string
#"strict" is deafult error, retrun "UnicodeDecodeError"
str_10 = "Ståle"
enc_10 = str_10.encode() #default using "utf-8" for encoding
print("Encodes the string by deafult 'utf-8': ", enc_10)
enc_10 =str_10.encode(encoding ="ascii", errors = "ignore") #ignore the the uncodeable unicode
print("Encodes the string with 'ignore' error: ", enc_10)
enc_10 = str_10.encode(encoding= "ascii", errors = "replace") #repalce the uncodeable unicode with "?"
print("Encodes the string with 'replace' error: ", enc_10)
enc_10 = str_10.encode(encoding= "ascii", errors = "xmlcharrefreplace") #insert a XML character reference 
print("Encodes the string with 'xmlcharrefreplace' error: ", enc_10)
enc_10 = str_10.encode(encoding="ascii", errors="backslashreplace") #inserts a \uNNNN escape sequence
print("Encodes the string with 'blackslashreplace' error: ", enc_10)
enc_10 = str_10.encode(encoding="ascii", errors="namereplace") #insert a N{...} escape sequence
print("Encodes the string with 'namereplace' error: ", enc_10)
print("------------------str_10_encoding_errors---------------------")

#endswith()
#return True value if string endswith with the given specified value, otherwise False
#endswith() take 3 parametera endswith, [value(required), start(optional, int), end(optional, int)]
str_11 = "Python.com"
end_str = str_11.endswith("m")
print(".endswith('m') return True if string endswith m else False: ", end_str)
end_str = str_11.endswith(".com")
print(".endswith('.com') return True if string endswith .com else False: ", end_str)
end_str = str_11.endswith("p")
print(".endswith('p') return True if string endswith p else False: ", end_str)
end_str = str_11.endswith(".com", 6, 10) #check if ".com" start and end by the given position. Note: Always write +1 for end position
print(".endswith('.com', 6, 10) return True if string endswith given position else False: ", end_str)
print("------------------str_11---------------------")

#startswith()
#return a True if the string start with the given specified value, otherwise Flase
#startswith(value, start, end)
str_12 = "Blender is use for 3d modelling and more"
start_str = str_12.startswith("b")
print(".startwith('b') return True if string startwith b else False: ", start_str)
start_str = str_12.startswith("B")
print(".startswith('B') return True if string startswith B else False: ", start_str)
start_str = str_12.startswith("is", 8, 10)
print(".startswith('is',8,10) return True if string startswith given positon else False: ", start_str)
start_str = str_12.startswith("blender", 0, 7)
print(".startswith('blender',0,7) return True if string startswith given positon else False: ", start_str)
start_str = str_12.startswith("Blender", 0, 7)
print(".startswith('Blender',0,7) return True if string startswith given positon else False: ", start_str)
print("------------------str_12---------------------")

#expandtabs()
#expandtab method replace "\t" with whitespaces 
#default tabsize is 8, syntax: [string.expands(tabsize)]
str_13 = "Hello\tWorld\tPython"
tb_str_13 = str_13.expandtabs() #default tabsize is 8
print("Expandtabs the string: ", tb_str_13)
tb_str_13 = str_13.expandtabs(10) #tabsize set to 10
print("Expandtabs the string by specified tabsize '10': ", tb_str_13)
tb_str_13 = str_13.expandtabs(25) #tabsize set to 10
print("Expandtabs the string by specified tabsize '25': ", tb_str_13)
print("------------------str_13---------------------")

#find()
#find method find the specified item and return the index number. If it's not able to find then return -1
str_14 = "Apple is fruit"
f_str_14 = str_14.find("p")
print(".find('p') finds the p in the string and return index no.: ", f_str_14)
f_str_14 = str_14.find("Apple")
print(".find('Apple') finds the Aple in the string and return index no.: ", f_str_14)
f_str_14 = str_14.find("f")
print(".find('f') finds the f in the string and return index no.: ", f_str_14)
f_str_14 = str_14.find("p", 1, 2)
print(".find('p',1,2) finds the p in the specified range and return index no.: ", f_str_14)
f_str_14 = str_14.find("e", 1, 4) #find method try to find "e" is coming in specified range or not
print(".find('e',1,4) finds the e in the specified range and return index no.: ", f_str_14, "(-1 means not found)")
print("------------------str_14---------------------")

#index()
#index method is almost same like find() method, the only difference is, when index method not able to find the item then it "raise an error"
str_15 = "Texturing"
i_str_15 = str_15.index("x")
print(".index('x') finds x and return index no. else throw an error: ", i_str_15)
'''i_str_15 = str_15.index("why") #raise an error
print(i_str_15)'''
print("------------------str_15---------------------")

#format()
#format method format a specified value inside the placeholders '{}'
str_16 = "My name is {} and i am {} years old" #empty placeholders
f_str_16 = str_16.format("Silk", 19)
print(".format('Silk', 19) formats a given value inside the placeholders '{}': ", f_str_16)
print(".format(lang = 'python!') formats a {lang} placeholder: ", "Welcome to {lang}".format(lang = "Python!")) #name indexes
print(".format('mango', 'king', 'fruits') formats a {0},{1},{2} index placeholders: ", "{0} is the {1} of the {2}".format("Mango", "king", "fruits")) #placeholders identified by indexes
print(".format('Apple', name = 'fruit') formats a {0},{name} name & index placeholders: ", "{0} is a {name}".format("Apple", name = "fruit")) #both placeholder 'index', and 'named'
print("------------------str_16---------------------")

#isalnum()
#isalnum method retrun True if string is a alphanumeric, otherwise False
#alphanumeric simply means word should contain alphabtes, numbers or both!
str_17 = "d12"
alpha_num = str_17.isalnum()
print(".isalnum('d12') return True if string is alphanumeric, else False: ", alpha_num)
print(".isalnum('python') return True if string is alphanumeric, else False: ", "python".isalnum())
print(".isalnum('1') return True if string is alphanumeric, else False: ", "1".isalnum())
print(".isalnum('DK ') return True if string is alphanumeric, else False: ", "DK ".isalnum()) #"space" is not alphanumeric that's why it return False
print("------------------str_17---------------------")

#isalpha()
#isalpha method return True if string is "alphabetic", otherwise False
str_18 = "alphabetic"
alphabetic = str_18.isalpha()
print(".isalpha('alphabetic') return True if string is alphabetic, else False: ", alphabetic)
print(".isalpha('Computer1234') return True if string is alphabetic, else False: ", "Computer1234".isalpha())
print(".isalpha('1') return True if string is alphabetic, else False: ", "1".isalpha())
print("------------------str_18---------------------")

#isascii()
#isascii method retrun True if all the characters in the string are ascii, otherwise Falses
str_19 = "bbs"
ascii_20 = str_19.isascii()
print(".isascii('bbs') return True if characters in the string are ascii, else False: ", ascii_20)
print(".isascii('Ståle') return True if characters in the string are ascii, else False: ", "Ståle".isascii())
print(".isascii('123') return True if characters in the string are ascii, else False: ", "123".isascii())
print("------------------str_19---------------------")

#isnumeric()
#isnumeric check all the character are numeric character or not
#numeric character is any Unicode symbol that represents a numeric value, and that includes fractions!
str_20 = "8011"
number = str_20.isnumeric()
print(".isnumeric('8011') return True if string is numeric, else False: ", number)
print(".isnumeric('Hench guy') return True if string is numeric, else False: ", "Hench guy".isnumeric())
print(".isnumeric('dk12') return True if string is numeric, else False: ", "dk12".isnumeric())
print(".isnumeric('\\u0047') return True if string is numeric, else False: ", "\u0047".isnumeric()) #\u0047 unicode of G
print(".isnumeric('⅕') return True if string is numeric, else False: ", "⅕".isnumeric())
print("------------------str_20---------------------")

#isdecimal()
#isdecimal method returns True, if the all characters are decimals characters(0-9), means the supercript, letters, signs are NOT decimal, it'll return False
#Use "isdecimal()" when you've to verify each and every char in the string from a base 10 number
str_21 = "110011"
decimal_20 = str_21.isdecimal()
print(".isdecimal('8011') return True if string contain decimals chars, else False: ", decimal_20)
print(".isdecimal('\\u0030') return True if it's a number unicode, else False: ", "\u0030".isdecimal()) #unicode for 0
print(".isdecima'\\u0047') return True if it's a number unicode, else False: ", "\u0047".isdecimal()) #unicode for G
print(".isdecimal('0030') return True if string contain decimals chars, else False: ", "0030".isdecimal())
print(".isdecimal('11') return True if string contain decimals chars, else False: ", "11 ".isdecimal()) #isdecimal cannot handle white space
print(".isdecimal('11d') return True if string contain decimals chars, else False: ", "11d".isdecimal()) 
print(".isdecimal('2²') return True if string contain decimals chars, else False: ", "2²".isdecimal(), "(.isdecimal cannot handle superscript)") #isdecimal cannot handle superscript
print("------------------str_21---------------------")

#isdigit()
#isdigit check that string contain all the digits or not, if yes then return True, otherwise False
#isdigit need special handling, such as "Superscript digits"
#isdigit works very well with unicodes only if unicode represent the digits
str_22 = "12"
digit_22 = str_22.isdigit()
print(".isdigit('12') return True if string all chars are digits, else Flase: ", digit_22)
print(".isdigit('g2') return True if string all chars are digits, else Flase: ", "g2".isdigit()) #if all char are not digit, return Flase
print(".isdigit('\\u0047') return True if string all chars are digits, else Flase: ", "\u0047".isdigit()) #unicode for G
print(".isdigit('\\u00B2') return True if string all chars are digits, else Flase: ", "\u00B2".isdigit()) #works with superscript and exponents even they're formatted in unicode verison(unicode of Cubed)
print(".isdigit('2²') return True if string all chars are digits, else Flase: ", "2²".isdigit()) #isdigit works with superscript
print(".isdigit('⅕') return True if string all chars are digits, else Flase: ", "⅕".isdigit(), "(.isdigit doesn't handle fractions)") #isdigit doesn't handle fractions (fractions in singal unicode value are not digits)
print("------------------str_22---------------------")

#isidentifier()
#isidentifier method valid identifier the string if only the string is alphanumeric, contain underscore, then it'll True
#isidentfier return False, if string contain space or start with number
str_23 = "Python_"
identify_23 = str_23.isidentifier()
print(".isidentifier('python_') return True if string is valid, else False: ", identify_23)
print(".isidentifier('08chp') return True if string is valid, else False: ", "08chp".isidentifier(), "(string cannot start with number)")
print(".isidentifier('hench guy and chp is the same person') return True if string is valid, else False: ", "hench guy and chp is the same person".isidentifier(), "(string containing space)")
print("------------------str_23---------------------")

#islower()
#islower return True if all the string chars are lowercase, otherwise False
str_24 = "abcd"
islower_24 = str_24.islower()
print(".islower('abcd') return True if all the chars are lowercase, else False: ", islower_24)
print(".islower('World') return True if all the chars are lowercase, else False: ", "World".islower())
print("------------------str_24---------------------")

#isupper()
#isupper return True if all the chars are uppercase, otherwise False
str_25 = "PYTHON"
isupper_25 = str_25.isupper()
print(".isupper('PYTHON') return True if all the chars are uppercase, else False: ", isupper_25)
print(".isupper('python') return True if all the chars are uppercase, else False: ", "Python".isupper())
print("------------------str_25---------------------")

#isprintbtable()
#isprintable return simply True, if all the char are printable
str_26 = "Omega"
printable_26 = str_26.isprintable()
print(".isprintable('Omega') return True if string is printable, else False:  ", printable_26)
print(".isprintable('#1') return True if string is printable, else False:  ", "#1".isprintable())
print(".isprintable('py\\nhello') return True if string is printable, else False:  ", "Py\nhello".isprintable(), "(\\n is not printable)") #\n is not printable
print(".isprintable('%d') return True if string is printable, else False:  ", "%d".isprintable())
print("------------------str_26---------------------")

#isspace()
#isspace return True, if string contain whitespace character, such as "  ", "\n", "\t", "\v", "\f"(feed), "\r"(carriage return), otherwise False
str_27 = " \n " #\n means newline
space_27 = str_27.isspace()
print(space_27)
print("ispace(' ') return True if string contain whitespace chars, else False: ", " ".isspace()) #space
print("ispace('\\v') return True if string contain whitespace chars, else False: ","\v".isspace()) #\v means vertical tab
print("ispace(' py ') return True if string contain whitespace chars, else False: ", " py ".isspace())
print("------------------str_27---------------------")

#istitle()
#istitle return True, if the string is "title-cased" means when word start with uppercase and the remaining chars are lowercase letters.
str_28 = "Zincovit"
title_28= str_28.istitle()
print("istitle('Zincovit') return True if string is title-cased, else False: ", title_28)
print("istitle('Python3.2') return True if string is title-cased, else False: ", "Python3.2".istitle()) #istitle ignore the number, and special chars
print("istitle('python') return True if string is title-cased, else False: ", "python".istitle())
print("------------------str_28---------------------")

#join()
#join the elements of a sequence and make it a new string
str_29 = "_"
join_29 = str_29.join("ABCD")
print(".join('_') join the specified element with the string and print a new string: ", join_29)
print(".join('.') join the specified element with the string and print a new string: ", ".".join("python"))
print(".join('//') join the specified element with the string and print a new string: ", "//".join("1,2,3,4"))
print("------------------str_29---------------------")

#ljust()
#ljust method left align the string by using specified character, (space " " is deafult as fill the character)
str_30 = "Hello, World!"
left_align_30 = str_30.ljust(20) #20 is the length
print(".ljust('Hello, World!') return a left-justified string: ", left_align_30)
print(".ljust('C++') return a left-justified string and filled the space by '1': ", "C++".ljust(30, "1")) #fill the space or padding it by "1"
print("------------------str_30---------------------")

#rjust()
#rjust method rigth align the string by using specified character, (space " " is default as fill the character)
str_31 = "hello, world"
rigth_align_31 = str_31.rjust(40)
print(".rjust('hello, world!') return a right-justified string: ", rigth_align_31)
print(".rjust('hello, world!') return a right-justified string and filled the space by 'O': ", "hello, world".rjust(40, "O"))
print("------------------str_31---------------------")

#lstrip
#lstrip remove the left side default space or specified character
str_32 = "           Java   script"
left_strip_32 = str_32.lstrip()
print(".lstrip('    Java   script') remove the left-side default space: ", left_strip_32)
print(".lstrip('P') remove the specified character 'p' from the string: ", "PPPPJavaScript".lstrip("P"))
print("------------------str_32---------------------")

#rstrip()
#lstrip remove the right side default space or specified character
str_33 = "     Cosmos   "
right_strip_33 = str_33.rstrip()
print(".rstrip('     Cosmos   ') remove the right-side default space: ", right_strip_33)
print(".rstrip('S') remove the specified character 'S' from the string: ", "ccccCosmosSSSSS".rstrip("S"))
print("------------------str_33---------------------")

#partition()
#partition mathod divide the string into 3 strings by seprator character and return into a  tuple
#and if seprator char is not found the it return empty strings at the end
str_34 ="NASA company is best for universal stuff"
partiton_34 = str_34.partition("best")
print(".partition('best') divide the string into 3 parts by seprator and return into a tuple: ", partiton_34)
print(".partition('cosmos') divide the string into 3 parts by seprator and return into a tuple: ", str_34.partition("cosmos"), "('cosmos' not found, return empty strings)") #seprator not found
print(".partition('ff') divide the string into 3 parts by seprator and return into a tuple: ", str_34.partition("ff"))
print("------------------str_34---------------------")

#removeprefix
#prefix remove the beginning of the word or group of word, and if word isn't present then it'll return copy of string
str_35 = "greece is beautiful"
prefix_35 = str_35.removeprefix("g")
print(".removeprefix('g') removed the prefix 'g' from the string: ", prefix_35)
print(".removeprefix('greece') removed the prefix 'greece' from the string: ", str_35.removeprefix("greece"))
print(".removeprefix('is') removed the prefix 'is' from the string, if not found return copy of the string: ", str_35.removeprefix("is")) #print copy of the string
print("------------------str_35---------------------")

#removesuffix
#suffix remove the ending of the word or group of word, and if word isn't present then it'll return copy of string
str_36 = "C language is hard"
suffix_36 = str_36.removesuffix("d")
print(".removesuffix('d') removed the suffix 'd' from the string: ", suffix_36)
print(".removesuffix('hard') removed the suffix 'hard' from the string: ", str_36.removesuffix("hard"))
print(".removesuffix('C') removed the suffix 'C' from the string, sif not found return copy of the string: ", str_36.removesuffix("C")) #print copy of the string
print("------------------str_36---------------------")

#replace() 
#replace method replace the old word with the new word
str_37 = "CSS, Java, Java, Java, Java"
replace_37 = str_37.replace("Java", "C++") #replace all
print(".replace('Java', 'C++') replace the old word with the new word from the string: ", replace_37)
print(".replace('Java', 'Python', 3) replace the old word with the new word from the string according to count: ", str_37.replace("Java", "Python", 3)) #replacing according to count
print("------------------str_37---------------------")

#rfind()
#rfind find the last appreance of the specified value, if not found return -1
str_38 = "Java and JavaScript is different language"
rfind_38 = str_38.rfind("Java") 
print(".rfind('Java') finds the last appreance of 'Java' in the string and return index no.: ", rfind_38)
print(".rfind('a',15,3) finds the last appreance of 'a' in specified range and return index no.: ", str_38.rfind("a", 5, 13)) #rfind method try to find last appreance of "a" in specified range
print(".rfind('q') finds the last appreance of 'q' in the string and return index no.: ", str_38.rfind("q"), "(-1 means not found in the string)") #return -1
print("------------------str_38---------------------")

#rindex
#rindex find the last appreance of the specified value, if not found it raise an error
str_39 = "Python, PHP"
rindex_39 = str_39.rindex("P")
print(".rindex('P') finds the last appreance of 'P' in the string, if not found it raise an error: ", rindex_39)
print(".rindex('y',0,5) finds the last appreance of 'y' in the specified range, if not found it raise an error: ", str_39.rindex("y", 0, 5)) #rindex method try to find last appreance of "y" in specified range then return the respective index no.
#print(str_29.rindex("q")) #raise an ValueError
print("------------------str_39---------------------")

#rpartition()
#rpartition divide the string into 3 part by specified char return into a tuple,
# if not found then it'll create empty strting at the start
str_40 = "Baking a cake"
rpart_40 = str_40.rpartition("B")
print(".rpartition('B') divides the string into 3 parts by specified char, if not found returns a empty string: ", rpart_40)
print(".rpartition('ke') divides the string into 3 parts by specified char, if not found returns a empty string: ", str_40.rpartition("ke"))
print(".rpartition('2') divides the string into 3 parts by specified char, if not found returns a empty string: ", str_40.rpartition("2")) #seprator not found
print("------------------str_40---------------------")

#split()
#split method spilt the string into a list, split it by space(default), or specifed seprator
#if maxsplit is specified then it start splitting from Left side char
str_41 = "Nice to meet you!"
split_41 = str_41.split()
print(".split() splits the string into a list by space(default): ", split_41)
print(".split('*') splits the string into a list by specified char: ", "Hello*universe*world".split("*"))
print(".split('*', 1) splits the string into a list by specified char: ", "Hello*universe*world".split("*", 1), "(maxsplit is 1 then it return 2 elements in the list)") #maxsplit is 1 then it return 2 elements in the list
print("------------------str_41---------------------")

#rsplit() 
#syntax: str.rplit(seprator[optional], mixsplit[optional])
#rsplit return a string into a list, starting from right, if seprator is not specified then it seprate by space(default)
#if maxsplit is specified then it start splitting from Right side char
str_42 = "Cooking a food"
rsplit_42  = str_42.rsplit()
print(".rsplit() splits a string from right side by space(default) and return into a list: ", rsplit_42)
print(".rsplit(',', 1) splits a string from right side by seprator and maxsplit and return into a list: ", "apple, mango, cherry, papaya, palm".rsplit(",", 1)) #setting the maxsplit to 1 means, return 2 elements in the list
print(".rsplit(',', 2) splits a string from right side by seprator and maxsplit and return into a list: ", "apple, mango, cherry, papaya, palm".rsplit(",", 2)) # return three elements in the list
print(".rsplit('_') splits a string from right side by seprator, if not found return copy of the string into list: ", "apple, mango, cherry, papaya, palm".rsplit("_")) #seprator not found return copy of the list
print("------------------str_42---------------------")

#splitlines()
#splitlines split the string into list, and split it by "\n"
str_43 = "Thanks for learning\n python"
slines_43 = str_43.splitlines()
print(".splitline() splits the string by '\\n' and return into a list: ", slines_43)
print(".splitline(True) splits the string by '\\n' but keep '\\n' and return into a list: ", "Python\n is awsome\n lanuage".splitlines(True)) #"True" means split the string but keep the "\n" (line break). Flase is default.
print("------------------str_43---------------------")

#swapcase()
#swapcase convert the uppercase into lowecase or lowercase into uppercase Characters
str_44 = "Hey, there!"
start_44 = str_44.swapcase()
print(".swapcase() converts the uppercase into lowercase or lowercase into uppercase: ", start_44)
print(".swapcase() converts the uppercase into lowercase or lowercase into uppercase: ", "hi, there!".swapcase())
print("------------------str_44---------------------")

#title()
#title make the first letter uppercase of each word
str_45 = "Tit or Tat"
title_45 = str_45.title()
print(".title() makes the first letter uppercase of each word: ", title_45)
print(".title() makes the first letter uppercase of each word: ", "i got 1st position in running".title())
print("------------------str_45---------------------")

#zfill()
#zfill add the zero at the beginning to make string long according to specified lengh
str_46 = "Dreamland"
zfill_46 = str_46.zfill(10)
print(".zfill(10) add zero at the beginning to make string long according to specified length: ", zfill_46)
print(".zfill(20) add zero at the beginning to make string long according to specified length: ", "Finally, done!".zfill(20))
print("------------------str_46---------------------")
