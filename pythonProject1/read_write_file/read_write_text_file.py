# OPEN METHOD
file = open('test.txt')

# READ METHOD - read all the contents of the file
var = file.read()
print(var)

# CLOSE METHOD - need to close to avoid memory leaks, once all the operations(read and write) are done
file.close()


# Reading only the first 5 character of the file by passing the parameter(number of characters)
file1 = open('test1.txt')
var1 = file1.read(5)
print(var1)
file1.close


# Read line method - read one single line of the txt file at a time
# each time the cursor is moving from one line to another line
file2 = open('test2.txt')
print(file2.readline())
print(file2.readline())
file2.close()


# Interview questions
# Print all the contents of the file, line by line using read line method.
file3 = open('test3.txt')
line3 = file3.readline()
while line3 != "":
    print(line3)
    line3 = file3.readline()      # To keep on scanning the next lines
file3.close()

# READLINES METHOD - stores the lines inside the text in the form of list
file4 = open('test4.txt')
for line in file4.readlines():
    print(line)

# WRITE METHOD
# STEP 1: read the file and store all the lines in the list
# STEP 2: reverse the list
# STEP 3: write back in the list
with open('test5.txt', 'r') as reader:      # r flag to set the mode as reader
    content = reader.readlines()    # list "content" stores all the lines
    reversed(content)   #Python reversed() method returns an iterator that accesses the given sequence in the reverse order
    with open('test5.txt','w') as writer:   # w flag to set the mode as writer
        for line in reversed(content):
            writer.write(line)




