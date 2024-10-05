# ITERATING OVER LIST USING FOR LOOP TO PRINT ALL THE ELEMENTS OF LIST
obj=[2,3,4,5,6,7,8]
for i in obj:
    print(i)

# PRINT MULTIPLES OF 2
obj=[2,3,4,5,6,7,8]
for i in obj:
    print(2*i)

# SUM OF FIRST 5 NATURAL NUMBERS
summation=0
for j in range(1,6):        # range(i,j) --> iterates from (i) to (j-1)
    summation = summation + j
print(summation)

# JUMP TWO VALUES FOR EACH ITERATION IN RANGE FUNCTION
print("************************************")
for k in range(1,10,2):
    print(k)

# PRINTING WITHOUT THE FIRST INDEX IN RANGE FUNCTION
print("************************************")
for m in range(10):
    print(m)

    