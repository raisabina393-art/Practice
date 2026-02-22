import os

try:
    filename = "example.txt"

    # 1. Create and Write
    with open(filename, "w") as file:
        file.write("First Line\n")

    print("After Writing:")
    with open(filename, "r") as file:
        print(file.read())

    # 2. Append
    with open(filename, "a") as file:
        file.write("Second Line\n")

    print("After Appending:")
    with open(filename, "r") as file:
        print(file.read())

    # 3. Show file properties using os
    print("File Size:", os.path.getsize(filename), "bytes")
    print("File Exists:", os.path.exists(filename))

except Exception as e:
    print("Error:", e)

finally:
    print("File operation completed.")