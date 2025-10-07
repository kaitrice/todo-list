tasks = []

def add(task_list):
  for task in task_list:
    tasks.append(task)

def remove(task_list):
  for task in task_list:
    if task in tasks:
      tasks.remove(task)

def complete(task_list):
  return

def print_tasks():
  print(f"\n{tasks}\n")

def print_func():
  print("\nCOMMANDS")
  print(" a <task> ... : add task(s)")
  print(" d <task> ... : delete task(s)")
  print(" c <task> ... : complete task(s)")
  print(" l : list tasks")
  print(" ? : print commands")
  print(" q : quit\n")
