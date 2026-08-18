tasks = []
completed_tasks = []

while True:
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Search Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        search = input("Enter task to search: ")
        found = False

        for task in tasks:
            if search.lower() in task.lower():
                print("Found:", task)
                found = True

        if not found:
            print("Task not found!")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to complete!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                completed = tasks.pop(number - 1)
                completed_tasks.append(completed)
                print("Task completed!")
            else:
                print("Invalid task number!")

    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                deleted = tasks.pop(number - 1)
                print("Task deleted:", deleted)
            else:
                print("Invalid task number!")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
