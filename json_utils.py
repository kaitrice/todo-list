import json
import os

from todo_utils import get_todo_lists, new_list


path = "todo/tasks.json"

def dump():
  todo_lists = get_todo_lists()
  with open("todo/tasks.json", 'w') as file:
    for name in todo_lists:
      tasks = todo_lists[name]
      json.dump(tasks, file)

def preload():
  isFile = os.path.isfile(path)
  if isFile:
    with open(path, 'r') as file:
      tasks = json.load(file)
      new_list("tasks", tasks)
