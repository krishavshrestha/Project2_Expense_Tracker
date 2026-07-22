# ==========================================
# Project 2 : Expense Tracker
# DecodeLabs Python Programming
# Developed by: Your Name
# ==========================================

# Variable to store total expense
total_expense = 0

print("===================================")
print("      EXPENSE TRACKER")
print("===================================")

# Infinite loop
while True:

    # Ask user to enter expense
    expense = input("\nEnter expense amount (or type 'done' to finish): ")

    # Stop the program if user enters done
    if expense.lower() == "done":
        break

    # Convert input into float
    expense = float(expense)

    # Add expense to total
    total_expense += expense

    # Display current total
    print(f"Current Total = Rs. {total_expense:.2f}")

print("\n===================================")
print(f"Total Expenses = Rs. {total_expense:.2f}")
print("Thank you for using Expense Tracker!")
print("===================================")