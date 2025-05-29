# Project 2: To-Do List App (Using Lists & Loops)

todo_list = []

while True:
    print("\nOptions: add, view, remove, exit")
    action = input("What would you like to do? ")

    if action == "add":
        task = input("Enter a task: ")
        todo_list.append(task)
    elif action == "view":
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. {task}")
    elif action == "remove":
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(todo_list):
            todo_list.pop(num - 1)
        else:
            print("Invalid task number.")
    elif action == "exit":
        break
    else:
        print("Try a valid option.")
