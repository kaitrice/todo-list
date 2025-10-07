todo_lists = {"tasks": {}}

# COMMANDS
def add(list_name, task_list):
  todo_list = get_list(list_name)
  for task in task_list:
    todo_list[task] = False

def remove(list_name, task_list):
  todo_list = get_list(list_name)
  for task in task_list:
    if task == '*':
      todo_list.clear()
    if task in todo_list:
      todo_list.pop(task)

def complete(list_name, task_list):
  todo_list = get_list(list_name)
  for task in task_list:
    todo_list[task] = True

# PRINTING
def print_tasks(list_name):
  print()
  for key, value in list_name.items():
    print(f"{key}: {value}")
  print()

def print_list(lists):
  for name in lists:
    if name in todo_lists:
      print_tasks(todo_lists[name])
    else:
      print(f"invalid list: {get_list_keys()}")

def print_lists():
  print(f"Lists: {get_list_keys()}")

def print_func():
  print("\nCOMMANDS")
  print(" a <list> <task> ... : add task(s) to list")
  print(" d <list> <task> ... : delete task(s) from list, use * to delete list")
  print(" c <list> <task> ... : complete task(s) from list")
  print(" n <list> ... : new list(s)")
  print(" p <list> : p list")
  print(" ? : print commands")
  print(" q : quit\n")

# GETTERS
def get_todo_lists():
  return todo_lists

def get_list(name):
  return todo_lists[name]

def get_list_keys():
  keys = []
  for key in todo_lists.keys():
    keys.append(key)
  return keys

# SETTERS
def new_list(name, items={}):
  todo_lists[name] = items