
# PRINTING FROM 0 TO 9 USING WHILE LOOP
i=0
while i<10:
    print(i)
    i = i + 1
print("While loop execution is done")

print("****************************************")

# SKIPPING 3 FROM 0 TO 9
j=0
while(j<10):
    if(j!=3):       # IF CONDITION TO SKIP THE 3
        print(j)
    j=j+1

# BREAK STATEMENT - to break the while loop abruptly
print("******** BREAK ************")
k=10
while(k>1):
    if(k==3):
        break
    print(k)
    k=k-1
print("While loop execution is done")

# CONTINUE STATEMENT - to skip the current iteration and proceed to next iteration
print("******* CONTINUE **************")
l=20
while(l>0):
    if(l==9):
        l=l-1
        continue
    if(l==17):
        l=l-1
        continue
    print(l)
    l=l-1

print("********* BREAK AND CONTINUE ********")
l=20
while(l>0):
    if(l==10):
        l=l-1
        continue
    if(l==7):
        break
    print(l)
    l=l-1






