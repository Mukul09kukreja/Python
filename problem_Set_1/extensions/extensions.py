def main():
    print(fileoutput())

def fileoutput():
    file = input("File name: ")
    if file.endswith(".gif"):
        return "image/gif"
    elif file.endswith(".jpg" or ".jpeg"):
        return "image/jpeg"
    elif file.endswith(".png"):
        return "image/png"
    elif file.endswith(".pdf"):
        return "application/pdf"
    elif file.endswith(".txt"):
        return "text/plain"
    elif file.endswith(".zip"):
        return "application/zip"
    
main()