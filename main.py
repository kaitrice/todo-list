tasks = []

def add(task):
  tasks.append(task)
  return

def remove(task):
  tasks.remove(task)
  return

def complete(task):
  return

def list():
  print(tasks)
  return

def print_func():
  print("\nCOMMANDS")
  print(" a <task> : add task")
  print(" d <task> : delete task")
  print(" c <task> : complete task")
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
        add(items[1])
      else:
        print("invalid syntax: a <task>")
    case 'd':
      if len(items) >= 2:
        remove(items[1])
      else:
        print("invalid syntax: d <task>")
    case 'c':
      if len(items) >= 2:
        complete(items[1])
      else:
        print("invalid syntax: c <task>")
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