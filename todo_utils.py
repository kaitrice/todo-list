from utils import get_todo_list


# LIST COMMANDS
def add(list_name, task_list):
  todo_list = get_todo_list(list_name)
  for task in task_list:
    todo_list[task] = False

def remove(list_name, task_list):
  todo_list = get_todo_list(list_name)
  for task in task_list:
    if task == '*':
      todo_list.clear()
    if task in todo_list:
      todo_list.pop(task)

def complete(list_name, task_list):
  todo_list = get_todo_list(list_name)
  for task in task_list:
    todo_list[task] = True

# PRINTING
def print_tasks(task_dict):
  print()
  for key, value in task_dict.items():
    print(f"{key}: {value}")
  print()
