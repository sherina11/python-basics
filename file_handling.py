file = open("sample.txt", "w")
file.write("Hello, this is Sherina learning Python!")
file.close()

file = open("sample.txt", "r")
content = file.read()
file.close()

print("File content:")
print(content)