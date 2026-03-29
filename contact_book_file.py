contacts = {}

try:
    file = open("contacts.txt", "r")
    for line in file:
        name, phone = line.strip().split(",")
        contacts[name] = phone
    file.close()
except FileNotFoundError:
    pass

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone

        file = open("contacts.txt", "a")
        file.write(name + "," + phone + "\n")
        file.close()

        print("Contact saved successfully!")

    elif choice == "2":
        if contacts:
            print("\nContacts List:")
            for name, phone in contacts.items():
                print(name, ":", phone)
        else:
            print("No contacts found!")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")