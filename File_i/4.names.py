name = input("What's your name? ")

file = open("File_i/4.names.txt", "a") # a used to append the file not rewrite again and again 
file.write(f"{name}\n")
file.close()
# so this code the file that we write is not look 
# ideal so how to fix it ? by using \n 

# Like sometimes you missed to close the file it become corupt or delted as per code
# So here we used new approach that you see in 5.names.py file