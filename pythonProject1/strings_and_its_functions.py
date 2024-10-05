str = "BarathCompany.com"

# we can break down string with each and every character by indexing
print(str[1])

# extracting part of string
print(str[0:6])

# Concatenate two strings
str1 = "Good "
str2 = "Morning"
str3 = str1 + str2
print(str1+str2)

# Checking the set of characters in the string
str4 = "Good Moring"
str5 = "Good"
print(str5 in str4)         # in function is used to check that

# Spliting the string with a character
str = "BarathCompany.com"
var=str.split(".")
print(var)
# split function divides the string and stores it in the form of list with index
print(var[1])

# Strip Method - to remove the white spaces in the beginning and ending of the string
str = "   Barath B   "
print(str.strip())
# Left Strip method - remove only the beginning white spaces of string
print(str.lstrip())
# Right Strip method - remove only the ending white spaces of string
print(str.rstrip())

