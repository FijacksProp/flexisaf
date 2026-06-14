from datetime import date


def get_amount():
    while True:
        amount_text = input("Amount: ").strip()

        try:
            amount = float(amount_text)
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount > 0:
            return amount

        print("Amount must be greater than zero.")


def add_expenses():
    expenses = []

    print("Enter expenses one after another.")
    print("Type 'exit' as the category when you are done.\n")

    while True:
        category = input("Category: ").strip()

        if category.lower() == "exit":
            break

        if not category:
            print("Category cannot be empty.")
            continue

        amount = get_amount()
        note = input("Note: ").strip()
        expense_date = input("Date (YYYY-MM-DD, optional): ").strip()

        if not expense_date:
            expense_date = date.today().isoformat()

        expenses.append(
            {
                "amount": amount,
                "category": category,
                "note": note,
                "date": expense_date,
            }
        )

        print("Expense added.\n")

    return expenses


def print_summary(expenses):
    if not expenses:
        print("No expenses were added.")
        return

    total = 0
    category_totals = {}

    print("\nAll Expenses")
    print("-" * 40)

    for index, expense in enumerate(expenses, start=1):
        total += expense["amount"]
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

        print(
            f"{index}. {expense['date']} | {category} | "
            f"{expense['amount']:.2f} | {expense['note']}"
        )

    print("\nSummary")
    print("-" * 40)
    print(f"Total spent: {total:.2f}")

    print("\nTotal by category:")
    for category, amount in category_totals.items():
        print(f"{category}: {amount:.2f}")


def main():
    expenses = add_expenses()
    print_summary(expenses)


if __name__ == "__main__":
    main()
