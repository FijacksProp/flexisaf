import json
from pathlib import Path


CONTACTS_FILE = Path(__file__).parent / "contacts.json"
contacts = {}
used_emails = set()
used_phones = set()


def load_contacts():
    global contacts

    if not CONTACTS_FILE.exists():
        return

    contacts = json.loads(CONTACTS_FILE.read_text(encoding="utf-8"))

    for contact in contacts.values():
        used_emails.add(contact["email"])
        used_phones.add(contact["phone"])


def save_contacts():
    json_text = json.dumps(contacts, indent=4)
    CONTACTS_FILE.write_text(json_text, encoding="utf-8")


def valid_email(email):
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if username == "" or domain == "":
        return False

    if "." not in domain:
        return False

    return True


def valid_phone(phone):
    clean_phone = phone.replace(" ", "").replace("-", "")
    return clean_phone.isdigit() and len(clean_phone) >= 7


def ask_email(current_email=None):
    while True:
        email = input("Email: ").strip().lower()

        if not valid_email(email):
            print("Please enter a valid email address.")
            continue

        if email in used_emails and email != current_email:
            print("That email is already used by another contact.")
            continue

        return email


def ask_phone(current_phone=None):
    while True:
        phone = input("Phone number: ").strip()

        if not valid_phone(phone):
            print("Please enter a valid phone number.")
            continue

        if phone in used_phones and phone != current_phone:
            print("That phone number is already used by another contact.")
            continue

        return phone


def add_contact():
    contact_id = input("Student ID or unique email: ").strip()

    if not contact_id:
        print("Unique identifier cannot be empty.")
        return

    if contact_id in contacts:
        print("A contact with this identifier already exists.")
        return

    full_name = input("Full name: ").strip()

    if not full_name:
        print("Full name cannot be empty.")
        return

    email = ask_email()
    phone = ask_phone()
    role = input("Role (Student, Parent, Teacher, Staff): ").strip().title()

    if not role:
        role = "Student"

    contacts[contact_id] = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "role": role,
    }

    used_emails.add(email)
    used_phones.add(phone)
    save_contacts()

    print("Contact added.")


def list_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return

    print("\nContacts")
    print("-" * 40)

    for contact_id, contact in contacts.items():
        print(f"ID: {contact_id}")
        print(f"Name: {contact['full_name']}")
        print(f"Email: {contact['email']}")
        print(f"Phone: {contact['phone']}")
        print(f"Role: {contact['role']}")
        print("-" * 40)


def search_contact():
    search_text = input("Search by ID, name, or email: ").strip().lower()

    for contact_id, contact in contacts.items():
        id_matches = search_text == contact_id.lower()
        name_matches = search_text in contact["full_name"].lower()
        email_matches = search_text == contact["email"].lower()

        if id_matches or name_matches or email_matches:
            print("\nContact found:")
            print(f"ID: {contact_id}")
            print(f"Name: {contact['full_name']}")
            print(f"Email: {contact['email']}")
            print(f"Phone: {contact['phone']}")
            print(f"Role: {contact['role']}")
            return

    print("No matching contact found.")


def update_contact():
    contact_id = input("Enter contact ID to update: ").strip()

    if contact_id not in contacts:
        print("Contact not found.")
        return

    contact = contacts[contact_id]
    old_email = contact["email"]
    old_phone = contact["phone"]

    print("Leave a field empty to keep the current value.")
    full_name = input(f"Full name ({contact['full_name']}): ").strip()
    role = input(f"Role ({contact['role']}): ").strip().title()

    change_email = input("Change email? (yes/no): ").strip().lower()

    if change_email == "yes":
        new_email = ask_email(current_email=old_email)
        used_emails.remove(old_email)
        used_emails.add(new_email)
        contact["email"] = new_email

    change_phone = input("Change phone? (yes/no): ").strip().lower()

    if change_phone == "yes":
        new_phone = ask_phone(current_phone=old_phone)
        used_phones.remove(old_phone)
        used_phones.add(new_phone)
        contact["phone"] = new_phone

    if full_name:
        contact["full_name"] = full_name

    if role:
        contact["role"] = role

    save_contacts()
    print("Contact updated.")


def delete_contact():
    contact_id = input("Enter contact ID to delete: ").strip()

    if contact_id not in contacts:
        print("Contact not found.")
        return

    contact = contacts.pop(contact_id)
    used_emails.remove(contact["email"])
    used_phones.remove(contact["phone"])
    save_contacts()

    print("Contact deleted.")


def show_menu():
    print("\nStudent Contact Manager")
    print("1. Add contact")
    print("2. Update contact")
    print("3. Delete contact")
    print("4. Search contact")
    print("5. List contacts")
    print("6. Exit")


def main():
    load_contacts()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            list_contacts()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please choose from 1 to 6.")


if __name__ == "__main__":
    main()
