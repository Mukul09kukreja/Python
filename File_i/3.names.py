name = input("What's your name? ")
# So here i am gonna use open
# Documentation of open is "docs.python.org/3/functions.html#open"
file = open("File_i/3.names.txt", "w") # w means here to write on file that i want to open
file.write(name)
file.close()
# So here it rewrite the file when run this code 