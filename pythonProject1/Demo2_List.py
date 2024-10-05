# List is a datatype that allows multiple values and can be of different datatypes
values = [1,2,3,4,5,"mass",78.265]

# Printing the elements of list based on the  index
print(values[0]) #printing first element
print(values[-1]) # printing last element
print(values[1:3])

# Insert function in Python
values.insert(3,"Barath")
print(values)

# Append function
values.append("End")
print(values)

# Updating the list is also possible
values[5] = "MASS"

# Delete function of list - deleting one index
del values[0]
print(values)

