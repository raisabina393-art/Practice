strr="Hello world"

with open("Example.txt", "w") as file:
    file.write(strr)

print("File written")

with open("Example.txt","a") as file:
    file.write("\n This is a new line")

file =open("Example.txt","r")
content= file.read()
print(content)
file.close()
 
