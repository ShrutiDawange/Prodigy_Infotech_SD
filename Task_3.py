import json
import os

def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    else:
        return {}

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    email = input("Enter the email address of the contact: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"{name} has been added to your contacts.")

def view_contacts(contacts):
    if contacts:
        print("Your Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Your contacts list is empty.")

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        print(f"Editing {name}:")
        phone = input("Enter the new phone number (leave blank to keep existing): ")
        email = input("Enter the new email address (leave blank to keep existing): ")
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        save_contacts(contacts)
        print(f"{name}'s information has been updated.")
    else:
        print(f"{name} is not in your contacts list.")

def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name} has been deleted from your contacts.")
    else:
        print(f"{name} is not in your contacts list.")

def main():
    contacts = load_contacts()

    while True:
        print("\nOptions:")
        print("1. Add a new contact")
        print("2. View contacts list")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
