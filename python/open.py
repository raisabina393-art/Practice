# File name
filename = "example.txt"

# Line you want to insert
new_line = "This is the inserted second line.\n"

# Open the file and read existing content
with open(filename, "r") as file:
    content = file.readlines()

# Insert the new line at a specific position (e.g., line 2)
position = 1   # Index starts from 0 (1 means second line)
content.insert(position, new_line)

# Write the updated content back to the file
with open(filename, "a") as file:
    file.writelines(content)

print("Line inserted successfully!")

