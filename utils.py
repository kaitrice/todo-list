# from json_utils import delete_file


todo_lists = {"tasks": {}}

def print_func():
  print("\nCOMMANDS")
  print(" a <list> <task> ... : add task(s) to list")
  print(" d <list> <task> ... : delete task(s) from list, use * to delete list")
  print(" c <list> <task> ... : complete task(s) from list")
  print(" n <list> : new list")
  print(" p <list> : p list, use * to print all list names")
  print(" ? : print commands")
  print(" q : quit\n")

# GETTERS
def get_todo_lists():
  return todo_lists

def get_todo_list(name):
  return todo_lists[name]

def get_list_keys():
  keys = []
  for key in todo_lists.keys():
    keys.append(key)
  return keys

# SETTERS
def new_list(name, items=None):
  if items is None:
    items = {}
  todo_lists[name] = items
  
def delete(list_name):
  from json_utils import delete_file
  if list_name in todo_lists:
    todo_lists.pop(list_name)
    delete_file(list_name)
