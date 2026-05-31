# ---------- Task Manager Application ----------

FILE_NAME = "tasks.txt"


class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status


tasks = []
task_counter = 1


# ---------- File Handling ----------
def save_tasks_to_file():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task.task_id}|{task.title}|{task.description}|{task.status}\n")


def load_tasks_from_file():
    global task_counter
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, description, status = line.strip().split("|")
                tasks.append(Task(int(task_id), title, description, status))
                task_counter = max(task_counter, int(task_id) + 1)
    except FileNotFoundError:
        pass


# ---------- CRUD OPERATIONS ----------
def create_task():
    global task_counter
    title = input("Enter task title: ")
    description = input("Enter task description: ")

    new_task = Task(task_counter, title, description)
    tasks.append(new_task)
    task_counter += 1

    save_tasks_to_file()
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        print("--------------------")
        print(f"ID: {task.task_id}")
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print(f"Status: {task.status}")


def update_task():
    task_id = int(input("Enter task ID to update: "))

    for task in tasks:
        if task.task_id == task_id:
            task.title = input("Enter new title: ")
            task.description = input("Enter new description: ")
            task.status = input("Enter status (Pending/Completed): ")
            save_tasks_to_file()
            print("Task updated successfully!")
            return

    print("Task not found.")


def delete_task():
    task_id = int(input("Enter task ID to delete: "))

    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            save_tasks_to_file()
            print("Task deleted successfully!")
            return

    print("Task not found.")


# ---------- EXTRA FEATURES ----------
def search_task():
    keyword = input("Enter keyword to search: ").lower()
    found = False

    for task in tasks:
        if keyword in task.title.lower():
            print("--------------------")
            print(f"ID: {task.task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Status: {task.status}")
            found = True

    if not found:
        print("No matching task found.")


def mark_completed():
    task_id = int(input("Enter task ID to mark completed: "))

    for task in tasks:
        if task.task_id == task_id:
            task.status = "Completed"
            save_tasks_to_file()
            print("Task marked as completed!")
            return

    print("Task not found.")


# ---------- MAIN PROGRAM ----------
load_tasks_from_file()

while True:
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Mark Task Completed")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        search_task()
    elif choice == "6":
        mark_completed()
    elif choice == "7":
        print("Exiting application.")
        break
    else:
        print("Invalid choice. Please try again.")

