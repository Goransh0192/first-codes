print("contact book".title())

contact_name = []

contact_number = []

def add_contact_name(name):
    name = input("Enter the name of the contact: ")
    contact_name.append(name)

def add_contact_number(number):
    number = input("Enter the contact number of the contact: ")
    contact_number.append(number)

def view_contact():
    if contact_name == []:
        print("No contacts found")
    else:
        print(contact_name)
        print(contact_number)

def remove_contact():
    name = input("Enter the name of the contact you want to remove: ")
    if name not in contact_name:
        print("Contact not found")
    else:
        contact_number.remove(contact_number[contact_name.index(name)])
        contact_name.remove(name)
        print("Contact removed")

running = True
while running:
    print("1. Add a contact\n2. Remove a contact\n3. View all contacts\n4. Exit the app")
    user_choice = input("Enter the Action: ")
    if user_choice == ("1"):
        add_contact_name(contact_name)
        add_contact_number(contact_number)
        print("Contact added")
    elif user_choice == ("2"):
        remove_contact()
    elif user_choice == ("3"):
        view_contact()
    elif user_choice == ("4"):
        running = False
    else:
        print("Invalid Input")
        continue
print("Thank you for using the Contact Book")
