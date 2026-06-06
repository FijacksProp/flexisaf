def get_number(prompt):
    while True:
        value_text = input(prompt).strip()

        try:
            return float(value_text)
        except ValueError:
            print("Please enter a valid number.")


def age_validator():
    age = get_number("Enter your age: ")

    if age >= 18:
        print("You are eligible because you are 18 or older.")
    else:
        print("You are not eligible yet because you are below 18.")


def login_flow():
    correct_username = "student"
    correct_password = "pass123"
    attempts = 3

    print("Demo login: username = student, password = pass123")

    while attempts > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username == correct_username and password == correct_password:
            print("Login successful.")
            return

        attempts -= 1
        print(f"Incorrect login details. Attempts left: {attempts}")

    print("Login failed. Please try again later.")


def loan_eligibility_checker():
    age = get_number("Age: ")
    monthly_income = get_number("Monthly income: ")
    credit_score = get_number("Credit score: ")
    has_existing_loan = input("Do you have an existing loan? (yes/no): ").strip().lower()

    is_adult = age >= 18
    earns_enough = monthly_income >= 50000
    good_credit = credit_score >= 650
    no_existing_loan = has_existing_loan == "no"

    if is_adult and earns_enough and good_credit and no_existing_loan:
        print("Loan status: Eligible")
    else:
        print("Loan status: Not eligible")
        if not is_adult:
            print("- Applicant must be at least 18.")
        if not earns_enough:
            print("- Monthly income should be at least 50,000.")
        if not good_credit:
            print("- Credit score should be at least 650.")
        if not no_existing_loan:
            print("- Existing loan must be cleared first.")


def expense_overspending_checker():
    threshold = get_number("Enter your spending threshold: ")
    total_expenses = 0

    while True:
        amount_text = input("Enter expense amount or 'done' to finish: ").strip()

        if amount_text.lower() == "done":
            break

        try:
            amount = float(amount_text)
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        total_expenses += amount

    print(f"Total expenses: {total_expenses:.2f}")
    if total_expenses > threshold:
        print("Warning: You have exceeded your spending threshold.")
    else:
        print("You are still within your spending threshold.")


def show_menu():
    print("\nDecision-Making Challenges")
    print("1. Age validator")
    print("2. Login flow")
    print("3. Loan eligibility checker")
    print("4. Expense overspending checker")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            age_validator()
        elif choice == "2":
            login_flow()
        elif choice == "3":
            loan_eligibility_checker()
        elif choice == "4":
            expense_overspending_checker()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
