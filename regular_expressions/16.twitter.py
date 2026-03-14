url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(username)

'''if we use input: My username is https://twitter.com/mukul09kukreja
so we get an output: My username is mukul09kukreja'''