Contacts = {}

while True:
    print("""Contact Book App
          1. Create Contact
          2. view all contacts
          3. Update Contact
          4. Delete Contact
          5. Search Contact
          6. Count Contact 
          7. Exit""")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the name: ")
        if name in Contacts:
            print(f"Contact name {name} already exists!")
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")
            Contacts[name] = {"age" : int(age), "email" : email, "mobile" : mobile }
            print(f"Contact name {name} has been created successfully!")

    elif choice == '2':
        if Contacts:
            print("All Contacts:")
            for name, contact in Contacts.items():
                print(f"Name: {name}, Age: {contact['age']}, Mobile: {contact['mobile']}, Email: {contact['email']}")
        else:
            print("No contacts available.")

        
    elif choice == '3':
        name = input("Enter name to update contact: ")
        if name in Contacts:
            age = input("Enter updated age: ")
            email = input("Enter updated email: ")
            mobile = input("Enter updated mobile number: ")
            Contacts[name] = {"age" : int(age), "email" : email, "mobile" : mobile }
        else:
            print("Contact not found!")

    elif choice == '4':
        name = input("Enter contact name to delete: ")
        if name in Contacts:
            del Contacts[name]
            print(f"Contact name {name} has been deleted successfully!")
        else:
            print("Contact not found!")
    
    elif choice == '5':
        search_name = input("Enter the name to search: ")
        found = False
        for name in Contacts:
            if search_name.lower() in name.lower():  
                contact = Contacts[name]  # Get the contact information
                print(f"Name: {name}, Age: {contact['age']}, Mobile: {contact['mobile']}, Email: {contact['email']}")
                found = True
        if not found:
            print(f"No contact found with the name {search_name}")


    elif choice == '6':
        print(f"Total contacts in your contact book : {len(Contacts)}")

    elif choice == '7':
        print("Thank you!")
        break

    else:
        print("Please Enter Valid Input!")  