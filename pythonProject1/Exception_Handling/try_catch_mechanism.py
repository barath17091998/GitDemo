

# TRY CATCH MECHANISM
try:
    with open('filelog.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)  # if the text file is present inside the folder, this will not come to the except block
finally:
    print("cleaning up resources")



