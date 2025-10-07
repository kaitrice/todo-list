from json_utils import dump, preload
from list_utls import print_list_names, print_lists
from todo_utils import add, complete, remove
from utils import new_list, print_func


print("~~ TODO LIST ~~")
preload()
print_list_names()
print_func()

items = input("enter a command: ").split()
cmd = items[0].lower()

while cmd != 'q':
  match cmd:
    case 'a':
      if len(items) >= 3:
        add(items[1], items[2:])
      else:
        print("invalid syntax: a <list> <task> ...")
    case 'd':
      if len(items) >= 3:
        remove(items[1], items[2:])
      else:
        print("invalid syntax: d <list> <task> ...")
    case 'c':
      if len(items) >= 3:
        complete(items[1], items[2:])
      else:
        print("invalid syntax: c <list> <task> ...")
    case 'n':
      if len(items) >= 2:
        new_list(items[1])
      else:
        print("invalid syntax: n <list>")
    case 'p':
      if len(items) >= 2:
        print_lists(items[1:])
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