assignments = []
expenses = []


def get_amount(prompt):
    while True:
        amount_text = input(prompt).strip()

        try:
            amount = float(amount_text)
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount > 0:
            return amount

        print("Amount must be greater than zero.")


def get_assignment_number(prompt):
    number_text = input(prompt).strip()

    if not number_text.isdigit():
        print("Please enter a valid number.")
        return None

    index = int(number_text) - 1

    if 0 <= index < len(assignments):
        return index

    print("Assignment number not found.")
    return None


def add_assignment():
    title = input("Assignment title: ").strip()
    due_date = input("Due date: ").strip()

    if title == "":
        print("Assignment title cannot be empty.")
        return

    assignment = {
        "title": title,
        "due_date": due_date,
        "completed": False,
    }

    assignments.append(assignment)
    print("Assignment added.")


def view_assignments():
    if len(assignments) == 0:
        print("No assignments yet.")
        return

    print("\nAssignments")
    for index, assignment in enumerate(assignments, start=1):
        if assignment["completed"]:
            status = "Done"
        else:
            status = "Pending"

        print(f"{index}. {assignment['title']} | Due: {assignment['due_date']} | {status}")


def mark_assignment_completed():
    view_assignments()

    if len(assignments) == 0:
        return

    index = get_assignment_number("Enter assignment number to mark completed: ")

    if index is None:
        return

    assignments[index]["completed"] = True
    print("Assignment marked as completed.")


def update_assignment():
    view_assignments()

    if len(assignments) == 0:
        return

    index = get_assignment_number("Enter assignment number to update: ")

    if index is None:
        return

    new_title = input("New title: ").strip()
    new_due_date = input("New due date: ").strip()

    if new_title != "":
        assignments[index]["title"] = new_title

    if new_due_date != "":
        assignments[index]["due_date"] = new_due_date

    print("Assignment updated.")


def remove_assignment():
    view_assignments()

    if len(assignments) == 0:
        return

    index = get_assignment_number("Enter assignment number to remove: ")

    if index is None:
        return

    removed_assignment = assignments.pop(index)
    print(f"Removed: {removed_assignment['title']}")


def add_expense():
    item = input("Expense item/category (lunch, transport, books, etc.): ").strip()

    if item == "":
        print("Expense item/category cannot be empty.")
        return

    amount = get_amount("Amount: ")
    expenses.append((item, amount))
    print("Expense added.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    print("\nExpenses")
    for index, expense in enumerate(expenses, start=1):
        item = expense[0]
        amount = expense[1]
        print(f"{index}. {item} | {amount:.2f}")


def filter_expenses_by_category():
    category = input("Category/item to filter by: ").strip().lower()

    matching_expenses = [
        expense for expense in expenses if expense[0].lower() == category
    ]

    if len(matching_expenses) == 0:
        print("No expenses found for that category.")
        return

    print("\nMatching expenses:")
    for item, amount in matching_expenses:
        print(f"{item} | {amount:.2f}")


def filter_expenses_above_amount():
    limit = get_amount("Show expenses above: ")

    expensive_items = [
        expense for expense in expenses if expense[1] > limit
    ]

    if len(expensive_items) == 0:
        print("No expenses are above that amount.")
        return

    print("\nExpenses above limit:")
    for item, amount in expensive_items:
        print(f"{item} | {amount:.2f}")


def show_menu():
    print("\nStudent Tasks and Expenses")
    print("1. Add assignment")
    print("2. View assignments")
    print("3. Mark assignment as completed")
    print("4. Update assignment")
    print("5. Remove assignment")
    print("6. Add expense")
    print("7. View expenses")
    print("8. Filter expenses by category")
    print("9. Show expenses above amount")
    print("10. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_assignment()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            mark_assignment_completed()
        elif choice == "4":
            update_assignment()
        elif choice == "5":
            remove_assignment()
        elif choice == "6":
            add_expense()
        elif choice == "7":
            view_expenses()
        elif choice == "8":
            filter_expenses_by_category()
        elif choice == "9":
            filter_expenses_above_amount()
        elif choice == "10":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please choose from 1 to 10.")


if __name__ == "__main__":
    main()
