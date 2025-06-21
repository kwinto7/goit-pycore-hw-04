
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact is added"

def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated"
    else:
        return f"Name {name} is not in your contacts. Add the new contact."

def show_phone(contact_name, contacts):
    if contact_name in contacts:
        return contacts[contact_name]
    else:
        return f"{contact_name} is not in your contacts"
    
def show_all(contacts):
   if not contacts:
    return "No contacts saved yet"
   else:
    result = "Your contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip() 

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command >>> ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Incorrect input! Please input in this format >>> add [name] [phone]")
            else:
                print(add_contact(args, contacts))
        elif command == "change":
            if len(args) != 2:
                print("Incorrect input! Please input in this format >>> change [name] [new_phone]")
            else:
                print(change_contact(args, contacts))
        elif command == "phone":
            if len(args) != 1:
                print("Incorrect input! Please input in this format >>> phone [name]")
            else:
                print(show_phone(args[0], contacts))
        elif command =="all":
            if args:
                print("Incorrect input! The 'all' command doesn't require any additional data.")
            else:
                print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()



