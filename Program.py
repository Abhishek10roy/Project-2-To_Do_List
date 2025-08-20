def task():
    tasks = []#empty list to store tasks
    print("******* WELCOME TO THE TO DO LIST APP *****")
    total_task = int(input("Enter the Number of Task:"))# user input for number of tasks
    for i in range(1, total_task + 1):# loop to get task names
        task_name = input(f"Enter the Task {i}=")# input for each task
        tasks.append(task_name)# adding task to the list
    print("******* YOUR TASKS ARE *******")

    print(f'Todays Tasks are \n {tasks}')

    while True:
        operation = int(input("Enter 1 for Add \nEnter 2 for Update \nEnter 3 for Delete \nEnter 4 for View \nEnter 5 for Exit or Stop \nEnter your choice="))
        if operation == 1:# adding a new task
            add = input("Enter Task you want to add=")
            tasks.append(add)# adding the new task to the list by using append function
            print(f'Task    Added Successfully!!!  ')
        elif operation == 2:# updating an existing task
            up= (input("Enter the Task you want to Update="))#to ask user for the task to update
            if up in tasks:#checking if the up exists in tasks
                index = tasks.index(up)# getting the index of the task to update
                new_task = input("Enter the New Task=")
                tasks[index] = new_task# updating the task at the index
                print(f'Task Updated Successfully!!! ')
            else:
                print("Task not found.")
        elif operation == 3:# deleting a task
            del_task = input("Enter the Task you want to Delete=")# to ask user for the task to delete
            if del_task in tasks:#checking if the del_task exists in tasks
                tasks.remove(del_task)#removing the task from the list
                print(f'Task Removed Successfully!!!')
            else:
                print("Task not found.")
        elif operation == 4:# viewing all tasks
            print(f'Todays Tasks are \n {tasks}')
        elif operation == 5:# exiting the application
            print("Exiting the To-Do List App. Goodbye!")
            break#using break to exit the loop

task()

# To-Do List Application
# This application allows users to manage their daily tasks by adding, updating, deleting, and viewing them.
# It uses a list to store tasks and provides a simple command-line interface for interaction.
