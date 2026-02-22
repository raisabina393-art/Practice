file=open("example.txt","r")
print("Filename:", file.name)
print("Filemode:",file.mode)
print(" Is file closing", file.closed)
file.close()
print("Is close?", file.closed)

