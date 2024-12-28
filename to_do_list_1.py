print (u'\u2713') # tick symbol
print((u'\u2717')) # cross symbol

import os 

#initialize an empt list for task

tasks = []


#function to displa tasks

def display_tasks():
    if not tasks:
        print("No task in the lsit.")
    else:
        print("\nTo-Do list:")
        #use forloop to fetch all the lists
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{index}. {task['description']} [{status}]")
    print()


#function to add task

def add_task():
    task_description = input("Enter the task description: ").strip()
    if task_description: 
        tasks.append({"description": task_description, "completed": False})
        print("Task addedd successfully")
    else:
        print("task description cannot be empty.")

#function for completet task
def complete_task():
    try:
        task_number = int(input("Enter the task no to mark as complete"))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print("Task marked as complete")
        else:
            print("Invalid task number")
    except ValueError:
        print("please enter a valid number.")


#we missed the delete_task()

def delete_task():
    try:
        task_number = int(input("Enter the task number to delete"))
        if 1 <=task_number <=len(tasks):
            tasks.pop(task_number - 1)
            print("Task delete successfully")
        else:
            print("Invalid task number.")
    except ValueError:
        print("please enter a valid number.")

#function to save task
def save_tasks():
    with open('tasks.txt', "w") as file:
        for task in tasks:
            file.write(f"{task['description']} | {task['completed']}\n")
    print("Tasks saved to 'tasks.txt'.")


#function to load tasks from a file
def load_tasks():
        if os.path.exists("/Users/aizaz/tasks.txt"): # set the file path where the txt file is saved
            with open("/Users/aizaz/tasks.txt","r") as file:
                for line in file:
                    description, completed = line.strip().split("|")
                    tasks.append({"description": description, "completed":completed == "True"})
            print("Tasks loaded successfully")
        else:
            print("No saved tasks found")



#now main menu loop

def main():
    load_tasks()
    while True:
        print("\nMenu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as complete")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Enter your choice").strip()

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

#now call the main functiojn


if __name__ == "__main__":
    main()