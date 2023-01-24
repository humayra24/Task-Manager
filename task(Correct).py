import uuid
from datetime import datetime

class Task:
  def __init__(self, task):
    self.task = task
    self.created_time = datetime.now()
    self.updated_time = None
    self.completed_time = None
    self.task_done = False
    self.id = uuid.uuid4()

  def update_task(self, task):
    self.task = task
    self.updated_time = datetime.now()

  def complete_task(self):
    self.task_done = True
    self.completed_time = datetime.now()

tasks = []

def add_task(task):
  tasks.append(task)
  print('\n')
  print("Task Created Successfully.")
  print('\n')
  print('*********************')
  print('\n')

def show_all_tasks():
  for task in tasks:
    print("ID: ", task.id)
    print("Task: ", task.task)
    print("Created Time: ", task.created_time)
    print("Updated Time: ", task.updated_time)
    print("Completed: ", task.task_done)
    print("Completed Time: ", task.completed_time)

  print('\n')
  print('*********************')
  print('\n')

def show_incomplete_tasks():
  for task in tasks:
    if not task.task_done:
      print("ID: ", task.id)
      print("Task: ", task.task)
      print("Created Time: ", task.created_time)
      print("Updated Time: ", task.updated_time)
      print("Completed: ", task.task_done)
      print("Completed Time: ", task.completed_time)

  print('\n')
  print('*********************')
  print('\n')

def show_completed_tasks():
  for task in tasks:
    if task.task_done:
      print("ID: ", task.id)
      print("Task: ", task.task)
      print("Created Time: ", task.created_time)
      print("Updated Time: ", task.updated_time)
      print("Completed: ", task.task_done)
      print("Completed Time: ", task.completed_time)
    elif task is None:
        print('No Completed Task')
        print('\n')
    

  print('\n')
  print('*********************')
  print('\n')

while True:
  print('\n')
  print("1. Add New Task")
  print("2. Show All Task")
  print("3. Show Incomplete Tasks")
  print("4. Show Completed Tasks")
  print("5. Update Task")
  print("6. Mark A Task Completed")
  print("0. To Exit!")
  print('\n')
  print("Enter Option: ", end="")
  option = int(input())
 

  if option == 0:
    print('\n')
    print("Exited!", end="")
    print('\n')
    print('*********************')
    print('\n')
    break

  if option == 1:
    print("Enter New Task: ", end="")
    task_name = input()
    task = Task(task_name)
    add_task(task)

  elif option == 2:
    show_all_tasks()

  elif option == 3:
    show_incomplete_tasks()

  elif option == 4:
    show_completed_tasks()

  elif option == 5:
    print("Enter Task ID: ", end="")
    task_id = input()
    task = next((value for value in tasks if value.id == task.id), None)
    if task is not None:
      print("Enter Updated Task: ", end="")
      updated_task_name = input()
      task.update_task(updated_task_name)
    else:
      print("Invalid Task ID!")
    

  elif option == 6:
    print("Enter Task ID: ", end="")
    task_id = input()
    task = next((value for value in tasks if value.id == task.id), None)
    if task is not None:
      task.complete_task()
    else:
      print("Invalid Task ID!")
    

  else:
    print('\n')
    print("Invalid Option!")
    print('\n')
    print('#################')
     
