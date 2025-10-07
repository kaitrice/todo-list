from todo_utils import print_tasks
from utils import get_list_keys, get_todo_lists


# PRINTING
def print_lists(list_names):
  for name in list_names:
    if name in get_todo_lists():
      print_tasks(get_todo_lists()[name])
    else:
      print(f"invalid list: {get_list_keys()}")

def print_list_names():
  print(f"Lists: {get_list_keys()}")
