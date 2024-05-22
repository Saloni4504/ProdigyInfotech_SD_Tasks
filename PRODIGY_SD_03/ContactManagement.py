import json
import os

# Define the filename for storing contacts
FILENAME = 'contacts.json'

def load_contacts():
    """Load contacts from the file."""
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    """View all contacts."""
    if contacts:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found.")

def edit_contact(contacts):
    """Edit an existing contact."""
    view_contacts(contacts)
    idx = int(input("Enter the number of the contact to edit: ")) - 1
    if 0 <= idx < len(contacts):
        contacts[idx]['name'] = input("Enter new name: ") or contacts[idx]['name']
        contacts[idx]['phone'] = input("Enter new phone number: ") or contacts[idx]['phone']
        contacts[idx]['email'] = input("Enter new email address: ") or contacts[idx]['email']
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

def delete_contact(contacts):
    """Delete a contact."""
    view_contacts(contacts)
    idx = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= idx < len(contacts):
        contacts.pop(idx)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

def main():
    contacts = load_contacts()

    while True:
        
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
