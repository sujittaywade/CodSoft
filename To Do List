# Example data structure for a to-do list
todo_list = [
    {"task": "Buy groceries", "status": "Not done"},
    {"task": "Finish homework", "status": "Not done"},
]
def add_task(task_name):
    todo_list.append({"task": task_name, "status": "Not done"})

def update_task_status(task_index, new_status):
    todo_list[task_index]["status"] = new_status

def display_todo_list():
    for index, task in enumerate(todo_list):
        print(f"{index + 1}. {task['task']} - {task['status']}")

def delete_task(task_index):
    del todo_list[task_index]
while True:
    print("To-Do List Menu:")
    print("1. Add task")
    print("2. Update task status")
    print("3. Display to-do list")
    print("4. Delete task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter the task name: ")
        add_task(task_name)
    elif choice == "2":
        display_todo_list()
        task_index = int(input("Enter the task index to update: ")) - 1
        new_status = input("Enter the new status: ")
        update_task_status(task_index, new_status)
    elif choice == "3":
        display_todo_list()
    elif choice == "4":
        display_todo_list()
        task_index = int(input("Enter the task index to delete: ")) - 1
        delete_task(task_index)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose a valid option.")
