from json_utils import dump, preload
from list_utls import print_list_names, print_lists
from todo_utils import add, complete, remove
from utils import delete, new_list, print_func

def main():
  print("~~ TODO LIST ~~")
  preload()
  print_list_names()
  print_func()

  items = input("enter a command: ").split()
  cmd = items[0].lower()

  while cmd != 'q':
    do_cmd(cmd, items)
    items = input("enter a command: ").split()
    cmd = items[0].lower()

  dump()

def do_add(list_name, task_list):
  if not list_name and not task_list:
    print("syntax error: a <list> <task> ...")
    return
  add(list_name, task_list)

def do_delete(list_name, task_list):
  if not list_name and not task_list:
    print("syntax error: d <list> <task> ...")
    return
  if task_list == ['*']:
    delete(list_name)
  else:
    remove(list_name, task_list)

def do_update(list_name, task_list):
  if not list_name and not task_list:
    print("syntax error: c <list> <task> ...")
    return
  complete(list_name, task_list)

def do_new(list_name):
  if not list_name:
    print("invalid syntax: n <list>")
    return
  new_list(list_name)

def do_print(list_name, lists):
  if not list_name:
    print("invalid syntax: p <list> ...")
    return
  if list_name == '*':
    print_list_names()
  else:
    print_lists(lists)

def do_cmd(cmd, items):
  length = len(items)
  list_name = items[1] if length >= 2 else ""
  task_list = items[2:] if length >= 3 else ""

  match cmd:
    case 'a':
      do_add(list_name, task_list)
    case 'd':
      do_delete(list_name, task_list)
    case 'c':
      do_update(list_name, task_list)
    case 'n':
      do_new(list_name)
    case 'p':
      do_print(list_name, items[1:])
    case '?':
      print_func()
    case _:
      print("invalid command")

if __name__:
  main()