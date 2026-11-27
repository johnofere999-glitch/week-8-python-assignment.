# Personal Mini-Toolkit
# Combines a persistent menu loop, conditionals, loops, and a dynamic list.


def todo_list_tool(tasks):
    """Lets the user view, add, or remove tasks in a live list."""
    while True:
        print("\n--- Quick To-Do List ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Back to main menu")

        action = input("Choose an option (1-4): ").strip()

        if action == "1":
            if not tasks:
                print("Your to-do list is currently empty.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")

        elif action == "2":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Added '{new_task}' to your list.")
            else:
                print("Task cannot be blank. Nothing was added.")

        elif action == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")
                try:
                    task_num = int(input("Enter the task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Removed '{removed}'.")
                    else:
                        print(f"Please enter a number between 1 and {len(tasks)}.")
                except ValueError:
                    print("Please enter a valid whole number.")

        elif action == "4":
            print("Returning to the main menu...")
            break

        else:
            print(f"'{action}' is not a valid option. Please choose 1 to 4.")


def grade_checker_tool():
    """Evaluates a score (0-100) and prints pass status and letter grade."""
    print("\n--- Pass & Grade Checker ---")
    try:
        score = float(input("Enter score (0-100): "))
    except ValueError:
        print("Invalid input. Please enter a numeric score.")
        return

    if score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        return

    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "PASSED" if score >= 50 else "FAILED"
    print(f"Score: {score} | Grade: {grade} | Status: {status}")


def multiplication_table_tool():
    """Prints the multiplication table (1 through 12) for a chosen number."""
    print("\n--- Multiplication Table Generator ---")
    try:
        number = int(input("Which number's table would you like to see? "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    print(f"\nMultiplication Table for {number}:")
    for multiplier in range(1, 13):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")


def main():
    tasks = []
    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n=== Personal Mini-Toolkit ===")
        print("1. Quick To-Do List")
        print("2. Pass & Grade Checker")
        print("3. Multiplication Table Generator")
        print("4. Quit")

        choice = input("Select a tool (1-4): ").strip()

        if choice == "1":
            todo_list_tool(tasks)
        elif choice == "2":
            grade_checker_tool()
        elif choice == "3":
            multiplication_table_tool()
        elif choice == "4":
            print("Thanks for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"'{choice}' is not on the menu. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
