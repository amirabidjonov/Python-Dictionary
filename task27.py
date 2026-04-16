from termcolor import colored

def phonebook_menu(phonebook: dict[str, str]) -> None:
    
    while True:
        print("\nPhonebook Menu:")
        print("1. Add contact")
        print("2. View contact")
        print("3. Search contact")
        print("4. Exit")


        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            phonebook[name] = phone
        
        elif choice == 2:
            name = input("Enter contact name: ")
            if name in phonebook:
                print(f"{name}: {phonebook[name]}")
            else:
                print("Contact not found.")
        
        elif choice == "3":
            search_name = input("Enter contact name: ")
            if search_name in phonebook:
                print(f"{search_name}: {phonebook[search_name]}")
            else:
                print("Contact not found.")
        
        elif choice == "4":
            print("Exiting phonebook menu.")
            break
        
        else:
            print("Invalid choice. Please try again.")
phonebook = {}
result = phonebook_menu(phonebook)

print(colored(f"result: {result}", "red"))

