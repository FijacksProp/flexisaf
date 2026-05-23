import json
from pathlib import Path


PROFILE_FILE = Path(__file__).parent / "profile.json"


def ask_required_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def ask_age():
    while True:
        age_text = input("Age: ").strip()
        if not age_text.isdigit():
            print("Age must be a number.")
            continue

        age = int(age_text)
        if 1 <= age <= 120:
            return age

        print("Please enter an age between 1 and 120.")


def ask_email():
    while True:
        email = input("Email: ").strip().lower()

        if email.count("@") != 1:
            print("Email must contain one @ symbol.")
            continue

        username, domain = email.split("@")

        if username == "" or domain == "":
            print("Email must have text before and after @.")
            continue

        if "." not in domain:
            print("Email domain must contain a dot, like example.com.")
            continue

        return email


def ask_phone():
    while True:
        phone = input("Phone number: ").strip()
        digits = phone.replace(" ", "").replace("-", "")

        if digits.isdigit() and len(digits) >= 7:
            return phone

        print("Please enter a valid phone number.")


def collect_profile():
    print("\nEnter your profile information")
    profile = {
        "full_name": ask_required_text("Full name: "),
        "age": ask_age(),
        "email": ask_email(),
        "phone": ask_phone(),
        "course": ask_required_text("Course/field of study: "),
        "school": ask_required_text("School name: "),
    }

    with open(PROFILE_FILE, "w", encoding="utf-8") as file:
        json.dump(profile, file, indent=4)

    print(f"Profile saved to {PROFILE_FILE.name}.")


def display_profile():
    if not PROFILE_FILE.exists():
        print("No saved profile found. Please create one first.")
        return

    with open(PROFILE_FILE, "r", encoding="utf-8") as file:
        profile = json.load(file)

    print("\nSaved Profile")
    print("-" * 30)
    print(f"Full name: {profile['full_name']}")
    print(f"Age: {profile['age']}")
    print(f"Email: {profile['email']}")
    print(f"Phone: {profile['phone']}")
    print(f"Course: {profile['course']}")
    print(f"School: {profile['school']}")


def show_menu():
    print("\nProfile Manager")
    print("1. Create or update profile")
    print("2. Display saved profile")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            collect_profile()
        elif choice == "2":
            display_profile()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
