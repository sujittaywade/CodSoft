import json

# Create a dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts()

# Function to view all contacts
def view_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print("-" * 20)
    else:
        print("No contacts found.")

# Function to search for a contact
def search_contact():
    name = input("Enter the name of the contact you want to search for: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
    else:
        print(f"{name} not found in contacts.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"{name} has been deleted from contacts.")
    else:
        print(f"{name} not found in contacts.")

# Function to save contacts to a JSON file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Function to load contacts from a JSON file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Main program loop
def main():
    global contacts
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu:")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

    print("Goodbye!")

if __name__ == "__main__":
    main()