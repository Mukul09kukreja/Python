phrase = input("camelCase: ")

words = []
for i in phrase:
    words.append(i)

for j in words:
    new_phrase = str(j)
    if j.isupper():  # Check if the original character is uppercase
        new_phrase = "_" + j.lower()  # Add underscore and lowercase it
    
    result = new_phrase.replace('\n', "")
    
    print(result.replace("\n", ""), end="")