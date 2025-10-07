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

def list():
  print(f"\n{tasks}\n")

def print_func():
  print("\nCOMMANDS")
  print(" a <task> ... : add task(s)")
  print(" d <task> ... : delete task(s)")
  print(" c <task> ... : complete task(s)")
  print(" l : list tasks")
  print(" ? : print commands")
  print(" q : quit\n")

print("~~ TODO LIST ~~")
print_func()

items = input("enter a command: ").split()
cmd = items[0].lower()

while cmd != 'q':
  match cmd:
    case 'a':
      if len(items) >= 2:
        add(items[1:])
      else:
        print("invalid syntax: a <task> ...")
    case 'd':
      if len(items) >= 2:
        remove(items[1:])
      else:
        print("invalid syntax: d <task> ...")
    case 'c':
      if len(items) >= 2:
        complete(items[1:])
      else:
        print("invalid syntax: c <task> ...")
    case 'l':
      list()
    case '?':
      print_func()
    case 'q':
      break
    case _:
      print("invalid command")
  
  items = input("enter a command: ").split()
  cmd = items[0].lower()