# Tydzień 2: Podstawy składni Pythona
# ✅ Zadanie: Poznaj podstawowe elementy składni Pythona — zmienne, typy danych, operatory, struktury danych, pętle i instrukcje warunkowe. 🔹 Kroki:

# Pracuj z typami danych: int, float, bool, str, list, dict, tuple, set.
# Stosuj operacje arytmetyczne i logiczne, wykorzystaj f-string do formatowania.
# Używaj pętli (for, while), instrukcji if, elif, else oraz list comprehensions.
# Zbuduj prosty projekt CLI do zarządzania zadaniami lub filtrowania wiadomości (in-memory).
# 🎯 Rezultat: Skrypt łączący podstawowe elementy składni języka.


def create_sample_tasks():
    """Create initial sample tasks for the task manager."""
    return [
        {
            "id": 1,
            "title": "my first todo",
            "description": "I have to do my first todo",
            "done": False,
        },
        {
            "id": 2,
            "title": "my second todo",
            "description": "I have to do my second todo",
            "done": False,
        }
    ]


def display_main_menu():
    """Display the main menu options."""
    print("""
          Welcome in Task Manager

          1. List and manage all tasks
          2. List only unfinished tasks
          3. Add task
          4. Exit
          """)


def display_tasks(tasks, show_all=True):
    """Display tasks in a formatted way."""
    if show_all:
        print("\nList all tasks:")
        tasks_to_show = tasks
    else:
        print("\nList unfinished tasks:")
        tasks_to_show = [task for task in tasks if not task["done"]]

    if not tasks_to_show:
        if show_all:
            print("No tasks available.")
        else:
            print("No unfinished tasks available.")
        return

    for task in tasks_to_show:
        status = "✅" if task["done"] else "❌"
        print(f"""
ID: {task["id"]}
Title: {task["title"]}
Description: {task["description"]}
Finished: {status}
""")


def find_task_by_id(tasks, task_id):
    """Find a task by its ID and return the task and its index."""
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return task, index
    return None, None


def display_task_management_menu():
    """Display task management options."""
    print("--------------------------------")
    print("")
    print("If you want to edit or delete task, please select id of the task")
    print("If you want to go back - please select option `back`")
    print("")


def display_task_actions_menu():
    """Display available actions for a selected task."""
    print("What you want to do with this task?")
    print("1. Mark as done")
    print("2. Edit")
    print("3. Delete\n")


def mark_task_as_done(task):
    """Mark a task as completed."""
    task["done"] = True
    print("Task marked as done")


def edit_task(task):
    """Edit task details."""
    print("--------------------------------")
    print("--------------------------------")
    print("Please enter new title of the task")
    new_title = input("New title: ")
    print("Please enter new description of the task")
    new_description = input("New description: ")
    print("Please enter new until date of the task")
    new_until = input("New until: ")

    task["title"] = new_title
    task["description"] = new_description
    task["until"] = new_until
    print("Task updated successfully")


def confirm_task_deletion():
    """Ask user to confirm task deletion."""
    print("--------------------------------")
    print("--------------------------------")
    print("Are you sure you want to delete this task?")
    print("1. Yes")
    print("2. No")
    return input("Select option: ")


def delete_task(tasks, task_index):
    """Delete a task from the tasks list."""
    confirmation = confirm_task_deletion()
    if confirmation == "1":
        tasks.pop(task_index)
        print("Task deleted successfully")
    elif confirmation == "2":
        print("Task not deleted")
    else:
        print("Invalid option")


def handle_task_action(tasks, task, task_index, action):
    """Handle the selected action for a task."""
    if action == "1":
        mark_task_as_done(task)
    elif action == "2":
        edit_task(task)
    elif action == "3":
        delete_task(tasks, task_index)
    else:
        print("Invalid option")


def manage_tasks(tasks, show_all=True):
    """Handle task listing and management."""
    display_tasks(tasks, show_all)

    # If showing only unfinished tasks and there are none, return early
    if not show_all and not any(not task["done"] for task in tasks):
        return

    display_task_management_menu()

    task_input = input("Select id of the task: ")
    if task_input == "back":
        return

    try:
        task_id = int(task_input)
        task, task_index = find_task_by_id(tasks, task_id)

        if task is None:
            print(f"Task with ID {task_id} not found!")
            return

        # If we're showing only unfinished tasks, check if the selected task is actually unfinished
        if not show_all and task["done"]:
            print(f"Task with ID {task_id} is already finished and not available in this view!")
            return

        print(f"You selected task with id: {task_input}\n")
        display_task_actions_menu()

        action = input("Select option: ")
        handle_task_action(tasks, task, task_index, action)

    except ValueError:
        print("Please enter a valid number for task ID!")


def get_next_task_id(tasks):
    """Generate the next available task ID."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_new_task(tasks):
    """Add a new task to the tasks list."""
    print("--------------------------------")
    print("--------------------------------")
    print("Please enter title of the task")
    title = input("Title: ")
    print("Please enter description of the task")
    description = input("Description: ")

    new_task = {
        "id": get_next_task_id(tasks),
        "title": title,
        "description": description,
        "done": False,
    }

    tasks.append(new_task)
    print("Task added successfully")


def main():
    """Main function to run the task manager."""
    tasks = create_sample_tasks()

    while True:
        display_main_menu()
        choice = input("Select option: ")

        if choice == "1":
            manage_tasks(tasks, show_all=True)
        elif choice == "2":
            manage_tasks(tasks, show_all=False)
        elif choice == "3":
            add_new_task(tasks)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid option! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
