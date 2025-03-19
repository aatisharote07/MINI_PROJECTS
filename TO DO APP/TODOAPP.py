def task():
    tasks=[]
    print("---------WELCOME TO THE TASK MANAGEMENT APP---------")
    total_task= int(input("How many task you want to add = "))
    for i in range(1,total_task+1):
            task_name=input(f"Enter task {i} =")
            tasks.append(task_name)
    print(f"Todays tasks are\n{tasks}")
    while True:
            operation=int(input("Enter\n 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop "))
            if operation ==1:
                add=input("Enter task you want to add: ")
                tasks.append(add)
                print(f"Task {add} has been successfully added....") 
            elif operation==2:
                  updated_val=input("Enter the Task you want to update= ")
                  if updated_val in tasks:
                        up=input("Enter the new Task= ")
                        ind=tasks.index(updated_val)
                        tasks[ind]=up
                        print(f"Updated Task {up}")
            elif operation==3:
                del_value=input("Enter the Task you want to Delete= ") 
                if del_value in tasks:
                    ind=tasks.index(del_value)
                    del tasks[ind]
                    print(f"Task {del_value} has been successfully deleted.")
                else:
                    print("Enter a Valid Task")
            elif operation==4:
                 print(f"Total tasks = {tasks}")    
            elif operation==5:
                print("Closing the program...")
                break

            else:
                print("Invalid input")
task()
