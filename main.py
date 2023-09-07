def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"
    return wrapper
def format_name(name):
    return name.capitalize()
def parse_command(command):
    parts = command.strip().lower().split()
    action = parts[0]
    args = parts[1:]
    return action, args
@input_error
def add_contact(contacts, name, phone):
    name = format_name(name)
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}"
@input_error
def change_contact(contacts, name, phone):
    name = format_name(name)
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} phone number changed to {phone}"
    else:
        raise IndexError
@input_error
def get_phone(contacts, name):
    name = format_name(name)
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        raise IndexError
@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found"
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
def handle_command(contacts, action, args):
    if action == "hello":
        return "How can I help you?"
    elif action == "add":
        return add_contact(contacts, *args)
    elif action == "change":
        return change_contact(contacts, *args)
    elif action == "phone":
        return get_phone(contacts, *args)
    elif action == "show":
        return show_all(contacts)
    elif action in ["close", "exit"]:
        return "Good bye!"
    else:
        return "Unknown command"
def main():
    print("Welcome to ContactBot!")
    contacts = {}
    while True:
        command = input("Enter a command: ")
        if command == ".":
            break
        action, args = parse_command(command)
        response = handle_command(contacts, action, args)
        print(response)
if __name__ == "__main__":
    main()