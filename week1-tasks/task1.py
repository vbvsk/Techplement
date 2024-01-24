import os
import json
from colorama import init, Fore
from prettytable import PrettyTable

init(autoreset=True)

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
        return contacts
    else:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=2)

def print_message(message, color=Fore.WHITE):
    print(color + message)

def add_contact(contacts, name, phone, email):
    errors = []

    if not name.isalpha():
        errors.append("Invalid name. Please enter a valid name.")

    if not phone.isdigit() or len(phone) != 10:
        errors.append("Invalid phone number. Please enter a 10-digit number.")

    # Basic email validation (you can use a more sophisticated method)
    if "@" not in email or "." not in email:
        errors.append("Invalid email address. Please enter a valid email.")

    if errors:
        for error in errors:
            print_message(error, Fore.RED)
    else:
        contacts[name] = {"Phone": phone, "Email": email}
        save_contacts(contacts)
        print_message(f"Contact '{name}' added successfully.", Fore.GREEN)

def search_contact(contacts, name):
    if name in contacts:
        contact = contacts[name]
        print_message(f"Contact Information for {name}:", Fore.CYAN)
        print_message(f"Phone: {contact['Phone']}")
        print_message(f"Email: {contact['Email']}")
    else:
        print_message(f"No contact found with the name '{name}'.", Fore.YELLOW)

def update_contact(contacts, name, phone, email):
    if name in contacts:
        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email
        save_contacts(contacts)
        print_message(f"Contact '{name}' updated successfully.", Fore.GREEN)
    else:
        print_message(f"No contact found with the name '{name}'.", Fore.YELLOW)

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print_message(f"Contact '{name}' deleted successfully.", Fore.GREEN)
    else:
        print_message(f"No contact found with the name '{name}'.", Fore.YELLOW)

def display_contacts(contacts):
    if not contacts:
        print_message("No contacts found.", Fore.YELLOW)
        return

    table = PrettyTable()
    table.field_names = ["Name", "Phone", "Email"]

    for name in sorted(contacts):
        contact = contacts[name]
        table.add_row([name, contact['Phone'], contact['Email']])

    print_message("All Contacts (Alphabetical Order):", Fore.CYAN)
    print(table)

def print_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts (Alphabetical Order)")
    print("6. Exit")

def main():
    contacts = load_contacts()

    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")
            add_contact(contacts, name, phone, email)

        elif choice == '2':
            name = input("Enter contact name to search: ")
            search_contact(contacts, name)

        elif choice == '3':
            name = input("Enter contact name to update: ")
            phone = input("Enter updated phone number: ")
            email = input("Enter updated email address: ")
            update_contact(contacts, name, phone, email)

        elif choice == '4':
            name = input("Enter contact name to delete: ")
            delete_contact(contacts, name)

        elif choice == '5':
            display_contacts(contacts)

        elif choice == '6':
            print_message("Exiting program.", Fore.BLUE)
            break

        else:
            print_message("Invalid choice. Please enter a valid option.", Fore.RED)

if __name__ == "__main__":
    main()

