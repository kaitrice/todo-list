from todo_utils import add, complete, print_func, print_list, remove
from json_utils import dump, preload


print("~~ TODO LIST ~~")
preload()
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
    case 'p':
      if len(items) >= 2:
        print_list(items[1:])
      else:
        print("invalid syntax: p <list> ...")
    case '?':
      print_func()
    case 'q':
      break
    case _:
      print("invalid command")
  
  items = input("enter a command: ").split()
  cmd = items[0].lower()

dump()