import os
file_path="example.txt"
if os.path.exists(file_path):
    print("Filename:", os.path.basename(file_path))
    print("Absolute path", os.path.abspath(file_path))
    print("size(bytes)", os.path.getsize(file_path))
    print("Is file?",os.path.isfile(file_path))
    print("Is directory", os.path.isdir(file_path))

else:
    print(f"The file '{file_path}' does not exist.")

    

