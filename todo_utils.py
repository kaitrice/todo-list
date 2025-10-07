tasks = {}
todo_lists = {}

# COMMANDS
def add(task_list):
  for task in task_list:
    tasks[task] = False

def remove(task_list):
  for task in task_list:
    if task == '*':
      tasks.clear()
    if task in tasks:
      tasks.pop(task)

def complete(task_list):
  for task in task_list:
    tasks[task] = True

# PRINTING
def print_tasks(list):
  print()
  for key, value in list.items():
    print(f"{key}: {value}")
  print()

def print_list(lists):
  for name in lists:
    print_tasks(todo_lists[name])

def print_func():
  print("\nCOMMANDS")
  print(" a <task> ... : add task(s)")
  print(" d <task> ... : delete task(s), use * to clear list")
  print(" c <task> ... : complete task(s)")
  print(" n <list> ... : new list(s)")
  print(" p <list> : p list")
  print(" ? : print commands")
  print(" q : quit\n")

# GETTERS
def get_todo_lists():
  return todo_lists

def get_list(name):
  return todo_lists[name]

# SETTERS
def new_list(name, items={}):
  todo_lists[name] = items