tasks = []
while True:
    print("Menu\n1. Add task\n2. View task\n3. Delete task\n4.Exit")
    choice = int(input("enter your choice"))
    if choice == 1:
        task = input("enter task which you have to add")
        tasks.append(task)
        print("task added")
    elif choice == 2:
        if len(tasks) == 0:
            print("no task found")
        else:
            print("your task")
            for index, task in enumerate(task,start = 1):
                print(f"{index}.{task}")
    elif choice == 3:
        if len(tasks) == 0:
            print("no task to be delete")
        else:
            for index , task in enumerate(tasks, start= 1 ):
                print(f"{index}.{task}")
            
            task_numbered = int(input("enter task number to delete"))
            if 1<=task_numbered<=len(task):
                removed_task = tasks.pop(task_numbered-1)
                print(f"delete:{removed_task}")
            else:
                print("invalid choice")
    elif choice == 4:
        print("good by")
        break
    else:
        print("invalid choice")
print("program ended")    

