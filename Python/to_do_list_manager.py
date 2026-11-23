tasks = []
while True:
    print("------To-Do List Manager------")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice (1-5):"))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue
    if choice<=0 or choice>5:
        print("Please choose from 1 to 5.")
        continue
    if choice == 1:
        task = input("Enter the task: ")
        if task.strip():
            tasks.append({"task": task.strip(), "status": "Pending"})
            print(f'Task "{task.strip()}" added successfully.')
        else:
            print("Task cannot be empty! Please enter a valid task.")
    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("Your Tasks:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['task']} - {task['status']}")
    elif choice == 3:
        if len(tasks)==0:
            print("No tasks available")
        else:
            print("Your Tasks:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['task']} - {task['status']}")
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["status"] = "Completed"
                    print(f'Task "{tasks[task_number - 1]["task"]}" marked as completed.')
                else:
                    print("Invalid task number! Please enter a valid task number.")
            except ValueError:
                print("Invalid input! Please enter a valid task number.")
    elif choice == 4:
        if len(tasks)==0:
            print("No tasks available")
        else:
            print("Your Tasks:")
            for index,task in enumerate(tasks):
                print(f"{index + 1}. {task['task']} - {task['status']}")
            try:
                task_number= int(input("Enter the task number to delete: "))
                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    print(f'Task "{deleted_task["task"]}" deleted successfully.')
                else:
                    print("Invalid task number! Please enter a valid task number.")
            except ValueError:
                print("Invalid input! Please enter a valid task number.")
    elif choice==5:
        print("Thank you for using the To-Do List Manager. Goodbye!")
        break