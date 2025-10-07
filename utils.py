import json
import os

tasks = {}
path = "tasks.json"

def add(task_list):
  for task in task_list:
    tasks[task] = False

def remove(task_list):
  for task in task_list:
    if task in tasks:
      tasks.pop(task)

def complete(task_list):
  for task in task_list:
    tasks[task] = True

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

def dump():
  with open("tasks.json", 'w') as file:
    json.dump(tasks, file)

def preload():
  global tasks
  isFile = os.path.isfile(path)
  if isFile:
    with open(path, 'r') as file:
      tasks = json.load(file)

preload()