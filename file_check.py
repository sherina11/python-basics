import os

filename = input("Enter file name: ")

if os.path.exists(filename):
    print("File exists")
else:
    print("File does not exist")