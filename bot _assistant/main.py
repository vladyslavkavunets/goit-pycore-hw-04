def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Use: add [name] [phone]"
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added"

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Use: change [name] [new_phone]"
    name, phone = args
    name_lower = name.lower()
    if name_lower not in contacts:
        return f"Contact {name} not found"
    contacts[name_lower] = phone
    return "Contact updated"

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid number of arguments. Usage: phone [name]"
    name = args[0]
    name_lower = name.lower()
    if name_lower not in contacts:
        return "Contact {name} not found"
    return contacts[name_lower]

def show_all(contacts):
    if not contacts:
        return "No contacts saved"
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    contacts = {}
    print("Welcome to the assistant bot")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "":
            continue
        else:
            print("Invalid command")
            
if __name__ == "__main__":
    main()