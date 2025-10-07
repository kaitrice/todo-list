import json
import os

from utils import get_todo_lists, new_list


path = "todo/"

def preload():
  for file in os.listdir(path):
    fullpath = os.path.join(path, file)
    with open(fullpath, 'r') as fp:
      tasks = json.load(fp)
      list_name = os.path.splitext(file)[0]
      new_list(list_name, tasks)

def dump():
  todo_lists = get_todo_lists()
  for name, tasks in todo_lists.items():
    filename = f"{name}.json"
    fullpath = os.path.join(path, filename)
    with open(fullpath, 'w') as file:
      json.dump(tasks, file, indent=2)
