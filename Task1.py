import json
import os
from datetime import datetime

def load_tasks():
    if os.path.exists('Mytasks.json'):
        with open('Mytasks.json', 'r') as taskdata:
            return json.load(taskdata)
    else:
        return 
def save_tasks(tasks):
    with open('Mytasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)


def Insert_task(tasks, description, priority, due_date):
    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")
    diff = today-due_date
    print(diff)


def delete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    removed_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Task removed: {removed_task['description']}")


def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    tasks[index]['completed'] = True
    save_tasks(tasks)
    print(f"Task marked as completed: {tasks[index]['description']}")


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{i + 1}. {task['description']} (Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status})")


def start():
    tasks = load_tasks()

    while True:
        print("What you wish to do \n")
        print("a. Add new task")
        print("b. Remove a task")
        print("c. Mark completed")
        print("d. List my tasks tasks")
        print("e. Quit")

        choice = input("Enter your choice:(a,b,c,d,e) ")

        if choice == 'a':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            Insert_task(tasks, description, priority, due_date)
        elif choice == 'b':
            index = int(input("Enter the task number to remove: ")) - 1
            delete_task(tasks, index)
        elif choice == 'c':
            index = int(input("Enter the task number to mark as completed: ")) - 1
            complete_task(tasks, index)
        elif choice == 'd':
            display_tasks(tasks)
        elif choice == 'e':
            break
        else:
            print("Invalid choice. Please enter using keytags(a,b,c,d,e)")

if __name__ == "__main__":
    a=input('Enter your name: ')
    print(f"hello, {a}")
    today = datetime.date.today()
    start()