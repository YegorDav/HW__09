import re

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name not in self.contacts:
            self.contacts[name] = phone
            return f"Added {name} with phone number {phone}"
        else:
            return f"Contact {name} already exists. Use 'change' command to update the phone number."

    def change_phone(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            return f"Changed phone number for {name} to {new_phone}"
        else:
            return f"Contact {name} not found"

    def find_phone(self, name):
        if name in self.contacts:
            return f"Phone number for {name} is {self.contacts[name]}"
        else:
            return f"Contact {name} not found"

    def show_all(self):
        return "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])

    def close(self):
        return "Good bye!"

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return wrapper

def parse_command(command):
    if command.lower() == "hello":
        return "hello"
    elif command.lower().startswith("add "):
        name, phone = command[4:].split(" ")
        return "add", name, phone
    elif command.lower().startswith("change "):
        name, phone = command[7:].split(" ")
        return "change", name, phone
    elif command.lower().startswith("phone "):
        name = command[6:]
        return "phone", name
    elif command.lower() == "show all":
        return "show all"
    elif command.lower() in ["good bye", "close", "exit"]:
        return "close"
    else:
        return "unknown"

def handle_command(contact_book, command):
    if command == "hello":
        return "How can I help you?"
    elif command[0] == "add":
        return contact_book.add_contact(command[1], command[2])
    elif command[0] == "change":
        return contact_book.change_phone(command[1], command[2])
    elif command[0] == "phone":
        return contact_book.find_phone(command[1])
    elif command == "show all":
        return contact_book.show_all()
    elif command == "close":
        return contact_book.close()
    else:
        return "Unknown command"

def main():
    contact_book = ContactBook()
    while True:
        command = input("Enter command: ")
        parsed_command = parse_command(command)
        if parsed_command == "close":
            print("Good bye!")
            break
        response = handle_command(contact_book, parsed_command)
        print(response)

if __name__ == "__main__":
    main()
