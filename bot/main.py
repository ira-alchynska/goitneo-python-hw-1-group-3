def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts saved.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").lower()  
        command, *args = user_input.split()

        if command == "close" or command == "exit":  
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2: 
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:  
            print(change_contact(args, contacts))
        elif command == "phone" and len(args) == 1:  
            print(show_phone(args, contacts))
        elif command == "all" and len(args) == 0:  
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
