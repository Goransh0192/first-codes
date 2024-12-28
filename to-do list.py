print("Task Manager")

storetasks = []
running=True
while running:
    print("1. Add a task\n2. Remove a task\n3. View all tasks\n4. Exit the app")
    user_choice = input("Enter the Action: ")
    if user_choice == ("1"):
        task = input("Enter the task: ".title())
        storetasks.append(task)
        print("Task added")
    elif user_choice == ("2"):
        task = input("Enter the task: ".title())
        if task not in storetasks:
            print("Task not found")
            continue
        else:
            storetasks.remove(task)
            print("Task removed")
    elif user_choice == ("3"):
        if storetasks == []:
            print("No tasks found")
        else:
            print(storetasks)
    elif user_choice == ("4"):
        running=False
    else:
        print("Invalid Input")
        continue
print("Thank you for using the Task Manager")